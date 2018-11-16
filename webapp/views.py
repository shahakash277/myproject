from django.shortcuts import render, redirect
from .forms import UserLoginForm, ProfileEditForm, SignUpForm
from .models import UserProfile
import traceback
from django.http import HttpResponse


# Create your views here.
def LoginRequest(request):
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            request.session['username'] = data.get('email')
            request.session['password'] = data.get('password')
            return redirect('/list')
        else:
            return render(request, 'login.html', {'form': login_form})
    else:
        login_form = UserLoginForm()
        return render(request, 'login.html', {'form': login_form})


def EditRequest(request):
    if checkIsAuthorized(request.session):
        user = UserProfile.objects.filter(email=request.session['username']).first()
        if request.method=='POST':
            edit_form = ProfileEditForm(data=request.POST)
            if edit_form.is_valid():
                return redirect(request, '/list')
        else :
            edit_form =ProfileEditForm(instance=user)
            return render(request, 'edit.html', {'form': edit_form})
    else:
        return redirect('/login')


def SignupRequest(request):
    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)
        if signup_form.is_valid():
            request.session['username'] = signup_form.cleaned_data['email']
            request.session['password'] = signup_form.cleaned_data['password']
            signup_form.save()
            return redirect('/list')
        else:
            return render(request, 'signup.html', {'form': signup_form})
    else:
        signup_form = SignUpForm()
        return render(request, 'signup.html', {'form': signup_form})


def ListRequest(request):
    if checkIsAuthorized(request.session):
        users = UserProfile.objects.all()
        return render(request, 'list.html', {'list_users': users})
    else:
        return redirect('/login')


def checkIsAuthorized(session):
    if 'username' in session and 'password' in session:
        user = UserProfile.objects.filter(email=session['username'], password=session['password']).first()
        if user is not None:
            return True
    return False


def LogOutResponse(request):
    request.session['username'] = ''
    request.session['passeord'] = ''
    login_form = UserLoginForm()
    return redirect('/login')
