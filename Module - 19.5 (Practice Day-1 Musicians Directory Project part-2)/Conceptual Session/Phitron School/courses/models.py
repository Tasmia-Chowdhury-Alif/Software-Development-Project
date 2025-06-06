from django.db import models
from django.contrib.auth.models import User
from .fields import OrderField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
class Course(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'courses_created')
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE, related_name= 'courses')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique= True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name= 'module')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = OrderField(blank=True, for_fields= ['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'
    
    
class Content(models.Model):
    module = models.ForeignKey(Module, on_delete= models.CASCADE, related_name= 'contents')
    content_type = models.ForeignKey(ContentType, 
                                    on_delete= models.CASCADE, 
                                    limit_choices_to={'model__in' : 
                                                      ('text', 
                                                       'video', 
                                                       'image', 
                                                       'file')}                                    
                                    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields= ['module'])

    class Meta:
        ordering = ['order']

    
