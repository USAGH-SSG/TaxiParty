from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .forms import LoginForm


# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        userId = form['username']
        userPw = form['password']
        user = authenticate(username=userId, password=userPw)
        if user:
            return redirect('')
        else:
            print("Wrong user credentials")
    
    context = {
        'form': form
    }
    return render(request, "login.html", context)