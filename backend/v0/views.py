from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

# function directs to homepage
def toIndex_view(request):
    return render(request, 'index.html')

# function directs to login page
def toLogin_view(request):
    return render(request, 'login.html')

# function directs to register page
def toRegister_view(request):
    return render(request, 'register.html')

def toUpload_view(request):
    return render(request, 'upload.html')

#function directs to the page after login
def afterLogin_view(request):
    # if "user" or "pwd" is not found, return an empty string
    email_input = request.POST.get("user", '')
    password_input = request.POST.get("pwd", '')

    if email_input and password_input:
        if userInfo.objects.filter(email = email_input, password = password_input).count() >= 1:
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Email address or password error.")
    else:
        return HttpResponse("Please enter your info.")
