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
            return render(request, "login.html", {'form': login_form})
    else:
        login_form = UserLoginForm()
        return render(request, 'login.html', {'form': login_form})


def EditRequest(request):
    if checkIsAuthorized(request.session):
        user=UserProfile.objects.get(email=request.session['username'])
        edit_form = ProfileEditForm(data=request.POST,instance=user)
        if edit_form.is_valid():
            return redirect(request, "/list")
        return render(request, "edit.html", {'form': edit_form})
    else:
        return redirect('/login')


def SignupRequest(request):
    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)
        if signup_form.is_valid():
            userProfile = UserProfile.toCreateModel(signup_form)
            userProfile.save()
            request.session['username'] = userProfile.email
            request.session['password'] = userProfile.password
            return redirect(request, "/list")
        else:
            return render(request, "signup.html", {'form': signup_form})
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
    print('gfgfg')

    if 'username' in session and 'password' in session:
        try:
            user = UserProfile.objects.filter(email=session['username'], password=session['password']).first()
            if user is not None:
                return True
        except:
            tb = traceback.format_exc()
            print('ddf')
            return HttpResponse(tb)

    return False


def LogOutResponse(request):
    request.session['username'] = ''
    request.session['passeord'] = ''
    login_form = UserLoginForm()
    return redirect('/login')
