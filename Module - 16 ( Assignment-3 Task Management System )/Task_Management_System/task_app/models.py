from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Task(models.Model):
    title = models.CharField(max_length=200)    
    description = models.TextField()
    task_assign_date = models.DateTimeField()
    # categories = models.ManyToManyField(Category)
    categories = models.ManyToManyField(Category, related_name='tasks')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    