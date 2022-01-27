from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=15)
    second_name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10,null=True,blank=True)
    address=models.TextField()
    panchayath=models.CharField(max_length=15)
    ward=models.IntegerField()
    house_no=models.IntegerField(primary_key=True)
    image=models.ImageField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.first_name
