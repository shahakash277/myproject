from django.db import models


# Create your models here.
class UserProfile(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.BigIntegerField
    dateOfBirth = models.DateField
    street1 = models.TextField
    street2 = models.TextField
    street3 = models.TextField
    state = models.TextField
    zip = models.IntegerField
    country = models.TextField
