from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm, CustomPasswordResetForm, CustomSetPasswordForm
from django.contrib.auth import logout
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required


# Create your views here.

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:dashboard')  # Redirect to home page after successful sign-in
    else:
        form = UserLoginForm()
    return render(request, 'authentication/signin.html', {'form': form})

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('main:dashboard')  # Redirect to home page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})

@unauthenticated_user
def recover(request):
    return render(request=request,
                  template_name="authentication/recover.html",
                  context={
                  })

def sign_out(request):
    logout(request)
    return redirect('authentication:signin')  # Redirect to home page after logout