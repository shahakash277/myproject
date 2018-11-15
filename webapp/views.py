from django.shortcuts import render, redirect
from .forms import UserLoginForm, ProfileEditForm,SignUpForm
from .models import UserProfile
import datetime

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


def edit(request):
    context = {}
    context['form'] = profileForm
    return render(request, 'edit.html', {'form': profileForm})


def LoginRequest(request):
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            return redirect('/edit')
        else:
            return render(request, "login.html", {'form': login_form})
    else:
        login_form = UserLoginForm()
        return render(request, 'login.html', {'form': login_form})


def EditRequest(request):
    if request.method == 'POST':
        edit_form = ProfileEditForm(data=request.POST)
        if edit_form.is_valid():

            return redirect('/edit')
        else:
            return render(request, "login.html", {'form': edit_form})
    else:
        edit_form = ProfileEditForm()
        return render(request, 'edit.html', {'form': edit_form})


def toModel(signup_form):
    userProfile =UserProfile()
    userProfile.email=signup_form.email


def toCreatel(signup_form):
        data= signup_form.cleaned_data

        userProfile = UserProfile()
        userProfile.email=data.get('email')
        userProfile.password=data.get('password')
        userProfile.firstName=data.get('firstName')
        userProfile.lastName=data.get('lastName')
        userProfile.phoneNumber=data.get('phoneNumber')
        userdate = data.get('datepicker')
        if userdate != '':
            userdate=datetime.datetime.strptime(userdate, "%m/%d/%Y").strftime("%Y-%m-%d")
            userProfile.dateOfBirth=userdate
        userProfile.street1=data.get('street_number')
        userProfile.street2=data.get('route')
        userProfile.street3=data.get('locality')
        userProfile.state=data.get('administrative_area_level_1')
        userProfile.country=data.get('country')
        userProfile.zip=data.get('postal_code')
        return  userProfile

def SignupRequest(request):
    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)
        if signup_form.is_valid():
            userprofile=toCreatel(signup_form)
            userprofile.save()
            return render(request, "signup.html")
        else:
            return render(request, "signup.html", {'form': signup_form})
    else:
        signup_form = SignUpForm()
        return render(request, 'signup.html',{'form':signup_form})
