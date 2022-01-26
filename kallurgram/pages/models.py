from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    first_name=models.CharField(max_length=15)
    second_name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField()
    phonenumber=PhoneNumberField(null=True,blank=True)
    address=models.TextField()
    panchayath=models.CharField(max_length=15)
    ward=models.IntegerField()
    house_no=models.IntegerField(primary_key=True)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.first_name
