import datetime

from django.db import models


# Create your models here.
class UserProfile(models.Model):
    email = models.CharField(primary_key=True,max_length=255)
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255,blank=True,null=True)
    lastName = models.CharField(max_length=255,blank=True,null=True)
    phoneNumber = models.BigIntegerField(blank=True,null=True)
    dateOfBirth = models.DateField(blank=True,null=True)
    street1 = models.TextField(blank=True,null=True)
    street2 = models.TextField(blank=True,null=True)
    street3 = models.TextField(blank=True,null=True)
    state = models.TextField(blank=True,null=True)
    zip = models.IntegerField(blank=True,null=True)
    country = models.TextField(blank=True,null=True)

