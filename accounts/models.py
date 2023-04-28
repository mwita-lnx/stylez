from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='vendor')
    location = models.CharField(max_length=50)
    description = models.TextField()
    contact_no = models.CharField(max_length=25)
    product_categories = models.CharField(max_length=50)
    comission_rate = models.IntegerField()
    profile_pic = models.ImageField(upload_to='accounts',null=True)

    

    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='customer')
    contact_no = models.CharField(max_length=25,null=True)


    

