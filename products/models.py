from django.db import models
from accounts.models import Vendor

# Create your models here.

class Product(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, primary_key=True)
    decription = models.TextField()
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=25)
    category = models.CharField(max_length=50)
    price = models.FloatField()
   
class Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='products',null=True)

   
class Subcategory(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=50)
