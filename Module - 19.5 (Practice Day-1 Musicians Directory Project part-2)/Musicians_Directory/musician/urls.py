from django.urls import path
from . import views

urlpatterns = [
    # path('', views.add_musician, name= 'AddMusician'),
    path('', views.AddMusician.as_view(), name= 'AddMusicianPage'),
    # path('edit_musician/<int:id>', views.edit_musician, name= 'EditMusicianPage'),
    path('edit_musician/<int:id>', views.EditMusician.as_view(), name= 'EditMusicianPage'),
    # path('delete_musician/<int:id>', views.delete_musician, name= 'DeleteMusicianPage'),
    path('delete_musician/<int:id>', views.DeleteMusician.as_view(), name= 'DeleteMusicianPage'),
]