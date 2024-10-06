from django.db import models
from .managers import CustomManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    objects = models.Manager() # by default it was it
    students = CustomManager()
    
