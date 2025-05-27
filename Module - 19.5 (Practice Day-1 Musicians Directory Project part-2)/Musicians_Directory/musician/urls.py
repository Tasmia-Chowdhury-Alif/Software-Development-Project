from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_musician, name= 'AddMusician'),
    path('edit_musician/<int:id>', views.edit_musician, name= 'EditMusician'),
    path('delete_musician/<int:id>', views.delete_musician, name= 'DeleteMusician'),
]