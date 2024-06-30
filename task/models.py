from django.db import models
import datetime
from category.models import Category
# Create your models here.
class Task(models.Model):
    Task_Title = models.CharField(max_length=100)
    Task_Category = models.ManyToManyField(Category)
    Task_Description =models.TextField()
    is_completed = models.BooleanField( default = False)
    Task_Assign_Date = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.Task_Title
    
