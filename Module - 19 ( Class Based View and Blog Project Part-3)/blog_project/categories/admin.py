from django.contrib import admin
from . import models

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)} # this attribute autometically fillup the slug field with the name field
    list_display = ['name', 'slug'] 

admin.site.register(models.Category, CategoryAdmin)