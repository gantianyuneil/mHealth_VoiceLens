from django.http import HttpResponse
from django.shortcuts import render

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
    username = request.POST.get("user", '')
    password = request.POST.get("pwd", '')

    if username and password:
        return HttpResponse("Login Successful!")
    else:
        return HttpResponse("Login Failed!")
