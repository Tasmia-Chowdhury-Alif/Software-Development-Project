from django.contrib import admin
from meals import models 

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Food)