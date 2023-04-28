from django.db import models
from ..accounts.models import Customer,Vendor
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, primary_key=True,related_name='ven')
    comission_rate = models.IntegerField()
    total = models.FloatField()
    transaction_id = models.CharField(max_length=100)
   


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField()

class ShippingInfo(models.Model):
     order =models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
     town =  models.CharField(max_length=100)
     estate = models.CharField(max_length=100)
     shipping_date = models.DateTimeField(default=timezone.now)
     delivered_date = models.DateTimeField(default=timezone.now)
     contact_no = models.CharField(max_length=25)
     shipped = models.BooleanField(default=False)
     delivered = models.BooleanField(default=False)
