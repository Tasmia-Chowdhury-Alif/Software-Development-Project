from django import forms 
from .models import Transaction 


class TransactionForm(forms.ModelForm):
    class Meta :
        model = Transaction
        fields = ['amount', 'transaction_type', 'sender_account_no', 'receiver_account_no']

    def __init__(self, *args, **kwargs):
        # user account object will be given as kwargs petameter
        self.account = kwargs.pop('account') # this contains an object of the User's UserBankAccount model
        super().__init__(*args, **kwargs)
        
        # making the transaction_type hidden for user in frontend. it will be handled maually
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput() 
        
        # making the transaction_type hidden for user in frontend. it will be handled maually
        self.fields['sender_account_no'].disabled = True
        self.fields['sender_account_no'].widget = forms.HiddenInput() 
        
        # making the transaction_type hidden for user in frontend. it will be handled maually
        self.fields['receiver_account_no'].disabled = True
        self.fields['receiver_account_no'].widget = forms.HiddenInput() 

    def save(self, commit= True):
        self.instance.account = self.account  # here self.instance is the instance or object of Transaction modelform. here in it's account field i am assigning the user_account object 
        self.instance.balance_after_transaction = self.account.balance  # balance_after_transection is being updated with new balance
        return super().save()


class DepositForm(TransactionForm):
    # this method is used to validate any form field's input data by naming the it as clean_fieldname
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        min_deposit_amount = 100

        if amount < min_deposit_amount :
            raise forms.ValidationError(f"Diposit Amount must be at least {min_deposit_amount} $")
        
        return amount
    
class WithdrawForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        account = self.account 
        min_withdraw_amount = 500
        max_withdraw_amount = 50000
        balance = account.balance

        if amount < min_withdraw_amount :
            raise forms.ValidationError(f"Withdraw Amount must be at least {min_withdraw_amount} $")

        if amount > max_withdraw_amount :
            raise forms.ValidationError(f"Withdraw Amount must be maximum {max_withdraw_amount} $")
        
        if balance < amount :
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount
    
class LoanForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        
        return amount
    

class TransferMoneyForm(TransactionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make 'note' visible and editable
        self.fields['receiver_account_no'].disabled = False
        self.fields['receiver_account_no'].widget = forms.NumberInput()

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        # transfer_account_no = self.cleaned_data["transfer_account_no"]
        account = self.account 
        min_transfer_amount = 500
        max_transfer_amount = 50000
        balance = account.balance 

        if amount < min_transfer_amount :
            raise forms.ValidationError(f"Money Transfer Amount must be at least {min_transfer_amount} $")

        if amount > max_transfer_amount :
            raise forms.ValidationError(f"Money Transfer Amount must be maximum {max_transfer_amount} $")
        
        if balance < amount :
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not transfer more than your account balance'
            )

        return amount