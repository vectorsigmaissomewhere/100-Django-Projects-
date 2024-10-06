from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True) you can't delete user as it is protecting page
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to ={'is_staff':True}) # now no-one can add pages 
    """Till now who we delete user pages will also get deleted, but now 
    deleting user will delete the user too, Reverse Relation for that we are using signal"""
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


# example of model inheritance
class Like(Page):
    panna = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()


    