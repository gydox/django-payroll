from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request=request,
                  template_name="authentication/login.html",
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