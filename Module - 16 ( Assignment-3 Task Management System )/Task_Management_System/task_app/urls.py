from django.urls import path, include 
from . import views 

urlpatterns = [
    path('add_task/', views.add_task, name= 'AddTaskPage'),
    path('edit_task/<int:id>', views.edit_task, name= 'EditTaskPage'),
    path('delete_task/<int:id>', views.delete_task, name= 'DeleteTaskPage'),
]