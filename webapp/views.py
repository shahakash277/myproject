from django.shortcuts import render, redirect
from .forms import UserLoginForm, ProfileEditForm

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


def SignupRequest(request):
    if request.method == 'POST':
        edit_form = ProfileEditForm(data=request.POST)
        if edit_form.is_valid():
            return redirect('/edit')
        else:
            return render(request, "login.html", {'form': edit_form})
    else:
        edit_form = ProfileEditForm()
        return render(request, 'edit.html', {'form': edit_form})
