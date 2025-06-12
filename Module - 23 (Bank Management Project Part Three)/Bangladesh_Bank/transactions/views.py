from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from accounts.models import UserBankAccount
from .forms import DepositForm, WithdrawForm, LoanForm, TransferMoneyForm
from .constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID, MONEY_TRANSFERED, MONEY_RECIVED
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.urls import reverse_lazy

def send_transaction_email(user, amount, subject, message_template):
    message = render_to_string(message_template, context={
        'user' : user, 
        'amount' : amount,
    })
    send_email = EmailMultiAlternatives(subject, to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = 'transactions/transaction_form.html'
    title = ''
    success_url = reverse_lazy('transaction-report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs.update({
            'account' : self.request.user.account
            })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'title' : self.title
        })
        return context
    

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit Form'

    def get_initial(self):
        initial = {'transaction_type' : DEPOSIT}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount 
        account.save(
            update_fields = ['balance']
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        # email_subject = "Deposit Message"
        # message = render_to_string('transactions/diposit_email.html', context={
        #     'user' : self.request.user, 
        #     'amount' : amount,
        # })
        # email_to = self.request.user.email
        # send_email = EmailMultiAlternatives(email_subject, to=[email_to])
        # send_email.attach_alternative(message, "text/html")
        # send_email.send()

        send_transaction_email(self.request.user, amount, "Deposit Message", 'transactions/diposit_email.html')

        return super().form_valid(form)
    

class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type' : WITHDRAWAL}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        if account.bank.is_bankrupt :
            messages.error(self.request, "Sorry, withdrawals are disabled because the bank is bankrupt.")
            return redirect("home")
        
        account.balance -= amount 
        account.save(
            update_fields = ['balance']
        )

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )

        send_transaction_email(account.user, amount, "Withdrawl Message", 'transactions/withdraw_email.html')

        return super().form_valid(form)
    

class LoanRequestView(TransactionCreateMixin):
    form_class = LoanForm
    title = "Loan Request"

    def get_initial(self):
        initial = {'transaction_type' : LOAN}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(account= self.request.user.account, transaction_type= 3, loan_approve= True).count()
        print(current_loan_count)

        if current_loan_count > 3 :
            return HttpResponse("You have excided the loan limits")
        
        messages.success(
            self.request,
            f'Loan request for {"{:,.2f}".format(float(amount))}$ submitted successfully'
        )

        send_transaction_email(self.request.user, amount, "Loan Request Message", 'transactions/loan_request_email.html')

        return super().form_valid(form)
    

class TransactionReportView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_report.html'
    balance = 0
    context_object_name = 'report_list' # by default ListView Class returns this as 'object_list' 

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account = self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            queryset = queryset.filter(timestamp__date__gte= start_date, timestamp__date__lte= end_date)
            self.balance = Transaction.objects.filter(timestamp__date__gte= start_date, timestamp__date__lte= end_date).aggregate(Sum(('amount')))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context

    
class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_transaction_id):
        loan_transaction = get_object_or_404(Transaction, id= loan_transaction_id)

        if loan_transaction.loan_approve :
            user_account = loan_transaction.account

            if loan_transaction.amount < user_account.balance :
                user_account.balance -= loan_transaction.amount
                user_account.save()

                loan_transaction.balance_after_transection = user_account.balance
                loan_transaction.transaction_type = LOAN_PAID
                loan_transaction.save()

                messages.success(self.request, "The loan is payed Successfully")
            else :
                messages.error(self.request, "Loan amount is greater than your account balance")

        return redirect('loan-list')
    

class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loan_transactions'

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account= user_account, transaction_type= LOAN)
        return queryset
    


class TransferMoneyView(TransactionCreateMixin):
    form_class = TransferMoneyForm
    template_name = 'transactions/money_transfer_form.html'
    title = 'Money Transfer'

    def get_initial(self):
        initial = {'transaction_type' : MONEY_TRANSFERED, 'sender_account_no' : self.request.user.account.account_no}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        
        receiver_account_no = form.cleaned_data.get('receiver_account_no')
        receiver_account = get_object_or_404(UserBankAccount, account_no= receiver_account_no)
        if receiver_account_no == account.account_no:
            messages.error(self.request, "You cannot transfer money to your own account.")
            return self.form_invalid(form)
        
        account.balance -= amount
        account.save(
            update_fields = ['balance']
        )
        receiver_account.balance += amount
        receiver_account.save(
            update_fields = ['balance']
        )

        # Create transaction record for receiver
        Transaction.objects.create(
            account= receiver_account,
            amount= amount,
            transaction_type= MONEY_RECIVED,
            balance_after_transaction = receiver_account.balance,
            receiver_account_no= receiver_account.account_no,
            sender_account_no= account.account_no,
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was Transfered to {receiver_account_no} successfully'
        )

        # sending email to Money Transferer (sender)
        send_transaction_email(self.request.user, amount, "Money Transfer Message", 'transactions/money_transfer_email.html')

        # sending email to Money Receiver 
        send_transaction_email(receiver_account.user, amount, "Money Recived Message", 'transactions/money_receive_email.html')

        return super().form_valid(form)
    

