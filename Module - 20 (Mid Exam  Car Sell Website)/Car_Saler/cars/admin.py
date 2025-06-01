from django.contrib import admin
from . import models 


class CarImageInline(admin.TabularInline):
    model = models.CarImage
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]

# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Comment)