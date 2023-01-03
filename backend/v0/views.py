from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

# function directs to homepage
def toIndex_view(request):
    return render(request, 'index.html')

# function directs to login page
def toLogin_view(request):
    return render(request, 'login.html')

# function directs to register page
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('psw', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        gender = request.POST.get('gender', '')
        race = request.POST.get('race', '')
        dob = request.POST.get('dob', '')
        first_language = request.POST.get('first_language', '')
        smoke = request.POST.get('smoke', '')

        # This User model is from Django package, not from own-built model
        user = userInfo(username=username, email=email, password=password, first_name=first_name, last_name=last_name, gender=gender, race=race, dob=dob, first_language=first_language, smoke=smoke)
        # Save user info to database
        user.save()
        print('user created')
        # redicrec to homepage
        return redirect('/v0')

    else:
        # when the request method is 'GET' 
        return render(request, 'register.html')

def toUpload_view(request):
    return render(request, 'upload.html')

#function directs to the page after login
def login_view(request):
    # if "user" or "pwd" is not found, return an empty string
    username_input = request.POST.get("username", '')
    password_input = request.POST.get("pwd", '')

    if username_input and password_input:
        if userInfo.objects.filter(username = username_input, password = password_input).count() >= 1:
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Email address or password error.")
    else:
        return HttpResponse("Please enter your info.")

