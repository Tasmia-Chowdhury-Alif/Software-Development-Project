from django.shortcuts import render
from .models import Transaction
from .forms import DipositForm, WithdrawForm, LoanForm
from .constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = ''
    title = ''
    success_url = ''

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
    

class DipositView(TransactionCreateMixin):
    form_class = DipositForm
    title = 'Diposit Form'

    def get_initial(self):
        initial = {'transaction_type' : DEPOSIT}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount 
        form.save(
            update_fields = ['balance']
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        return super().form_valid(form)
    
    