from django import forms

from user.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'name', 'password1', 'password2']
        widgets = {'name': forms.TextInput(attrs={'size': 20}),}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)