from django.urls import path, include
from . import views

urlpatterns = [
    # path('add/', views.add_post, name= 'AddPost'),
    path('add/', views.AddPostView.as_view(), name= 'AddPost'),
    # path('edit/<int:id>', views.edit_post, name= 'EditPost'),
    path('edit/<int:id>', views.EditPostView.as_view(), name= 'EditPost'),
    # path('delete/<int:id>', views.delete_post, name= 'DeletePost'),
    path('delete/<int:id>', views.DeletePostView.as_view(), name= 'DeletePost'),
]