from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT) # doing this user cannot be deleted
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # doing this if user is deleted post cannot be deleted6  
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()