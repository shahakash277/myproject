from django.shortcuts import render
from .forms import UserRegistrationForm, ProfileEditForm
from .models import UserProfile
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


def edit(request):
    profileForm = ProfileEditForm(data=request.POST)
    context = {}
    context['form'] = profileForm
    return render(request, 'edit.html',{'form':profileForm})


def LoginForm(request):
    login_form = UserRegistrationForm(data=request.POST)
    return render(request, 'login.html',{'form':login_form})
