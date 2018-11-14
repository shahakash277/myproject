from django import forms
from .models import UserProfile


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

        try:
            user = UserProfile.objects.get(email=email, password=password)
            if user is None:
                raise forms.ValidationError({'email': 'Invalid email or password.'})
        except:
            raise forms.ValidationError({'email': 'Invalid email or password.'})
        return data


class ProfileEditForm(forms.ModelForm):
    email = forms.CharField(label='email', widget=forms.TextInput)

    class Meta:
        model = UserProfile
        fields = ['email', 'password']


class SignUpForm(forms.ModelForm):
    email = forms.CharField(label='email', widget=forms.TextInput)
