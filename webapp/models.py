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

    @staticmethod
    def toCreateModel(signup_form):
        userProfile = UserProfile()
        userProfile.email=signup_form.email
        userProfile.password=signup_form.password
        userProfile.firstName=signup_form.firstName
        userProfile.lastName=signup_form.lastName
        userProfile.phoneNumber=signup_form.phoneNumber
        userProfile.dateOfBirth=signup_form.datepicker
        userProfile.street1=signup_form.street_number
        userProfile.street2=signup_form.route
        userProfile.street3=signup_form.locality
        userProfile.state=signup_form.administrative_area_level_1
        userProfile.country=signup_form.country
        userProfile.zip=signup_form.postal_code
