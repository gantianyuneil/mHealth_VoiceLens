from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout, authenticate
import html


# Create your views here.

# function directs to homepage
def toIndex_view(request):
    return render(request, 'index.html')

# function directs to login page
def toLogin_view(request):
    return render(request, 'login.html')

# function directs to personal profile page
def toProfile_view(request):
    return render(request, 'personal.html' )

# function directs to register page
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('psw', '')
        password2 = request.POST.get('psw2', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        gender = request.POST.get('gender', '')
        race = request.POST.get('race', '')
        dob = request.POST.get('dob', '')
        first_language = request.POST.get('first_language', '')
        smoke = request.POST.get('smoke', '')
        
        if username and email and password1 and password2 and first_name and last_name and dob:
            if password1 == password2:
                # salt and hash password (for security)
                hashed_pw = make_password(password1)

                if userInfo.objects.filter(username=username).exists():
                    # It means the username is already existed.
                    # We are printing this message to html so that user can see.
                    messages.info(request,'Username Taken')
                    return redirect('/v0/register/')
                else:
                    user = userInfo(username=username, email=email, password=hashed_pw, first_name=first_name, last_name=last_name, gender=gender, race=race, dob=dob, first_language=first_language, smoke=smoke)
                    # Save user info to database
                    user.save()
                    print('user created')
                    # redicrect to homepage
                    return redirect('/v0')
            else:
                # password and confirmed password are not matching
                messages.info(request,"Password doesn't match")
                return redirect('/v0/register/')
        else:
            # It means user doesn't fill out the complete registration form
            messages.info(request,'Register Information Misses!')
            return redirect('/v0/register/')

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

    if userInfo.objects.filter(username=username_input).exists():
        #user's password from database
        # user_pwd = userInfo.objects.filter(username=username_input).values_list('password', flat=True).first()
        # to check if the username and password are both matched
        if username_input and password_input:
            # user login with authentication
            user = authenticate(request, username=username_input, password=password_input)
            if user is not None:
                # user successfully login and redirect to homepage
                login(request, user)
                return redirect('/v0')
            else:
                messages.info(request, 'Username or password do not match')
                return redirect('/v0/login/')
        else:
            messages.info(request, 'Username or password do not match')
            return redirect('/v0/login/')
    else:
        messages.info(request, "Username doesn't exist")
        return redirect('/v0/login/')

def logout_view(request):
    logout(request)
    return redirect('/v0')
