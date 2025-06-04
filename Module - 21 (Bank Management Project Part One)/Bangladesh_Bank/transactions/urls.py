from django.urls import path 
from .views import DepositMoneyView, WithdrawMoneyView, TransactionReportView, LoanRequestView, PayLoanView, LoanListView

urlpatterns = [
    path('deposit/', DepositMoneyView.as_view() , name= 'deposit'),
    path('withdraw/', WithdrawMoneyView.as_view() , name= 'withdraw'),
    path('transaction_report/', TransactionReportView.as_view() , name= 'transaction-report'),
    path('loan_request/', LoanRequestView.as_view() , name= 'loan-request'),
    path('loans/', LoanListView.as_view() , name= 'loan-list'),
    path('pay_loan/<int:loan_transaction_id>/', PayLoanView.as_view() , name= 'pay-loan'),
]