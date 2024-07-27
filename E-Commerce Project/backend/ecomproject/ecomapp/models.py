from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # when I delete the user all the product of the user is deleted
    productname = models.CharField(max_length=150)
    image = models.ImageField(null=True,blank=True, upload_to="images")
    productbrand = models.CharField(max_length=100,null=True,blank=True)
    productcategory = models.CharField(max_length=100,null=True,blank=True)
    productinfo = models.TextField()
    rating = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True,blank=True)
    stockcount = models.IntegerField(null=True, blank=True,default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.productname