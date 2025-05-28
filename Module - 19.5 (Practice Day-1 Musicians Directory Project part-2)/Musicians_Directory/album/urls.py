from django.urls import path
from . import views

urlpatterns = [
    # path('', views.add_album, name= 'AddAlbumPage'),
    path('', views.AddAlbum.as_view(), name= 'AddAlbumPage'),
    # path('edit_album/<int:id>', views.edit_album, name= 'EditAlbumPage'),
    path('edit_album/<int:id>', views.EditAlbum.as_view(), name= 'EditAlbumPage'),
]