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
        data = signup_form.cleaned_data
        userProfile = UserProfile()
        userProfile.email = data.get('email')
        userProfile.password = data.get('password')
        userProfile.firstName = data.get('firstName')
        userProfile.lastName = data.get('lastName')
        userProfile.phoneNumber = data.get('phoneNumber')
        userdate = data.get('datepicker')
        if userdate != '':
            userdate = datetime.datetime.strptime(userdate, "%m/%d/%Y").strftime("%Y-%m-%d")
            userProfile.dateOfBirth = userdate
        userProfile.street1 = data.get('street_number')
        userProfile.street2 = data.get('route')
        userProfile.street3 = data.get('locality')
        userProfile.state = data.get('administrative_area_level_1')
        userProfile.country = data.get('country')
        userProfile.zip = data.get('postal_code')
        return userProfile
