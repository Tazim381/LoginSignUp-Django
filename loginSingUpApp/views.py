from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .forms import register_form,login_form
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    return render(request,'loginSignUpApp/home.html',{'username':username})

def register(request):
    if request.method=="POST":
        form =register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Errors are :",form.errors)
    form = register_form()
    return render(request,'loginSignUpApp/register.html',{'form':form})

def login(request):
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)

            user = authenticate(request,username= username, password= password)
            print(user)
            if user:
                auth_login(request, user)
                return redirect('home')
    form = login_form()
    return render(request,'loginSignUpApp/login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required()
def addItem(request):
    return render(request,'loginSignUpApp/addItem.html')