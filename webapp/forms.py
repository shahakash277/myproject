import datetime

from django import forms
from .models import UserProfile
import re


def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class UserLoginForm(forms.ModelForm):
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = UserProfile
        fields = ['email', 'password']

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        password = data.get('password')

        if not validateEmail(email):
            raise forms.ValidationError({'email': 'Invalid Email'})

        user = UserProfile.objects.filter(email=email, password=password).first()
        if user is None:
            raise forms.ValidationError({'email': 'Invalid email or password.'})

        return data


class ProfileEditForm(forms.ModelForm):
    datepicker = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'id': 'dateOfBirth', 'autocomplete': 'off', 'placeholder': ''}))
    street_number = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'id': 'street_number', 'placeholder': 'Street Address, P.O box, etc.'}))
    route = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'id': 'route', 'placeholder': 'Apt, Suite, Unit, etc.'}))
    locality = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'id': 'locality', 'placeholder': 'Area, Region.'}))
    administrative_area_level_1 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'id': 'administrative_area_level_1', 'placeholder': 'ity, Village'}))
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'country', 'placeholder': 'Conutry'}))
    postal_code = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'id': 'postal_code', 'placeholder': 'zip code, postal code.'}))

    class Meta:
        model = UserProfile
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        password = data.get('password')
        confirmPassword = data.get('confirmPassword')
        phoneNumber = data.get('phoneNumber')
        datepicker = data.get('datepicker')

        if not validateEmail(email):
            raise forms.ValidationError({'email': 'Invalid Email'})

        if password != confirmPassword:
            data['password'] = ''
            data['confirmPassword'] = ''
            raise forms.ValidationError({'password': 'Password and Confirm Password does not Match.'})

        if phoneNumber is not None and len(str(phoneNumber)) != 0 and len(str(phoneNumber)) != 10:
            raise forms.ValidationError({'phoneNumber': 'Phone Number is Invalid. Contain only 10 digit'})

        if datepicker != '' and bool(
                re.search('^(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/[0-9]{4}$', datepicker)) != True:
            raise forms.ValidationError({'datepicker': 'Invalid date please Insert in mm/dd/yyyy '})
        return data

    def save(self, commit=True):
        data = self.cleaned_data
        userProfile =UserProfile.objects.filter(data.get('email')).first()
        userProfile.firstName = data.get('firstName')
        userProfile.lastName = data.get('lastName')
        userProfile.phoneNumber = data.get('phoneNumber') if 'phoneNumber' in data else 0
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


class SignUpForm(forms.ModelForm):
    datepicker = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'id': 'dateOfBirth', 'autocomplete': 'off', 'placeholder': ''}))
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput())
    street_number = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'id': 'street_number', 'placeholder': 'Street Address, P.O box, etc.'}))
    route = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'id': 'route', 'placeholder': 'Apt, Suite, Unit, etc.'}))
    locality = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'id': 'locality', 'placeholder': 'Area, Region.'}))
    administrative_area_level_1 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'id': 'administrative_area_level_1', 'placeholder': 'ity, Village'}))
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'country', 'placeholder': 'Conutry'}))
    postal_code = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'id': 'postal_code', 'placeholder': 'zip code, postal code.'}))

    class Meta:
        model = UserProfile
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        password = data.get('password')
        confirmPassword = data.get('confirmPassword')
        phoneNumber = data.get('phoneNumber')
        datepicker = data.get('datepicker')

        if not validateEmail(email):
            raise forms.ValidationError({'email': 'Invalid Email'})

        if password != confirmPassword:
            data['password'] = ''
            data['confirmPassword'] = ''
            raise forms.ValidationError({'password': 'Password and Confirm Password does not Match.'})

        if phoneNumber is not None and len(str(phoneNumber)) != 0 and len(str(phoneNumber)) != 10:
            raise forms.ValidationError({'phoneNumber': 'Phone Number is Invalid. Contain only 10 digit'})

        if datepicker != '' and bool(
                re.search('^(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/[0-9]{4}$', datepicker)) != True:
            raise forms.ValidationError({'datepicker': 'Invalid date please Insert in mm/dd/yyyy '})

        user = UserProfile.objects.filter(email=email).first()
        if user:
            raise forms.ValidationError({'email': 'Email Id is already Register'})
        return data

    def save(self, commit=True):
        data = self.cleaned_data
        userProfile = UserProfile()
        userProfile.email = data.get('email')
        userProfile.password = data.get('password')
        userProfile.firstName = data.get('firstName')
        userProfile.lastName = data.get('lastName')
        userProfile.phoneNumber = data.get('phoneNumber') if 'phoneNumber' in data else 0
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

        if commit:
            userProfile.save()



