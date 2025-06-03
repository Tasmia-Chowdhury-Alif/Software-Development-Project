from django.urls import path 
from .views import DipositMoneyView, WithdrawMoneyView, TransactionReportView, LoanRequestView, PayLoanView, LoanListView

urlpatterns = [
    path('diposit/', DipositMoneyView.as_view() , name= 'DipositPage'),
    path('withdraw/', WithdrawMoneyView.as_view() , name= 'WithdrawPage'),
    path('transaction_report/', TransactionReportView.as_view() , name= 'TransactionReportPage'),
    path('loan_request', LoanRequestView.as_view() , name= 'LoanRequestPage'),
    path('loans', LoanListView.as_view() , name= 'LoanListPage'),
    path('pay_loan/<int:loan_transaction_id>', PayLoanView.as_view() , name= 'PayLoanPage'),
]