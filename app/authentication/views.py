from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def signin(request):
    return render(request=request,
                  template_name="authentication/signin.html",
                  context={
                  })

def register(request):
    return render(request=request,
                  template_name="authentication/register.html",
                  context={
                  })

def recover(request):
    return render(request=request,
                  template_name="authentication/recover.html",
                  context={
                  })