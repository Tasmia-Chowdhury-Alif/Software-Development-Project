from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import DepositForm, WithdrawForm, LoanForm
from .constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.urls import reverse_lazy

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
        account.balance -= amount 
        account.save(
            update_fields = ['balance']
        )

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )

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
    


