from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username', widget=forms.TextInput)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    class Meta:
        model = UserProfile
        fields = '__all__'

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'