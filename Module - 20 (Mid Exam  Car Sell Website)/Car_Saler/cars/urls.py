from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>/', views.CarDetailsView.as_view(), name= 'DetailsPage'),
    path('car/<int:pk>/buynow/', views.BuyNowView.as_view(), name= 'BuyNowPage'),
]
