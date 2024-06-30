from django.db import models

# Create your models here.
class Category(models.Model):
    Category_Name = models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.Category_Name
    