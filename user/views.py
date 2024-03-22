from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import LoginForm, SignupForm


# Create your views here.
def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('user:login'))

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        userId = form.cleaned_data['username']
        userPw = form.cleaned_data['password']
        user = authenticate(request, username=userId, password=userPw)
        if user:
            login(request, user)
            return redirect('../../')
        else:
            messages.warning(request, "Wrong user credentials")
    
    context = {
        'form': form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect(reverse('user:login'))