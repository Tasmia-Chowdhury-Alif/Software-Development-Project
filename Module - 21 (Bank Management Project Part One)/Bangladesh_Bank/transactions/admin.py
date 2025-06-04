from django.contrib import admin
from .models import Transaction

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'timestamp', 'loan_approve']


    def get_readonly_fields(self, request, obj = None):
        # when a new object of Transaction is being created, this obj = None by default. but when the object is created this method will receve it as paramete. so then the obj is no longer None.

        if obj and obj.loan_approve :
            # Make loan_approve read-only only after it's set to True for first time
            return self.readonly_fields + ('loan_approve',)

        return super().get_readonly_fields(request, obj)

    def save_model(self, request, obj, form, change):
        if obj.loan_approve :
            obj.account.balance += obj.amount
            obj.account.save()
            obj.balance_after_transaction = obj.account.balance
            obj.save()

        return super().save_model(request, obj, form, change)
