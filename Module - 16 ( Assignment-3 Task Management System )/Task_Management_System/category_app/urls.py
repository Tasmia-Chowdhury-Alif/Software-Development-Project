from django.urls import path, include 
from . import views 

urlpatterns = [
    path('add_category/', views.add_category, name= 'AddCategoryPage'),
    # path('edit_category/<int:id>', views.edit_category, name= 'EditCategoryPage'),
    # path('delete_category/<int:id>', views.delete_category, name= 'DeleteCategoryPage'),
]