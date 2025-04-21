from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add_post, name= 'AddPost'),
    path('edit/<int:id>', views.edit_post, name= 'EditPost'),
    path('delete/<int:id>', views.delete_post, name= 'DeletePost'),
]