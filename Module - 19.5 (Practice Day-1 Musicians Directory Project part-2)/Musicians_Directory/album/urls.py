from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_album, name= 'AddAlbum'),
    path('edit_album/<int:id>', views.edit_album, name= 'EditAlbum'),
]