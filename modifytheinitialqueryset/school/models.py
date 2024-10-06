from django.db import models
from .managers import CustomManager
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    # objects = models.Manager() # default ModelManager be objects in views but CustomMangager will also work
    students = CustomManager() # now the name will come by order
    
