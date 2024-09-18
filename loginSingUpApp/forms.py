from django import  forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)