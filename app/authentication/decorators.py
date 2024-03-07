# decorators.py

from django.shortcuts import redirect
from django.urls import reverse

def unauthenticated_user(view_func):
    """
    Decorator to restrict access to a view only to unauthenticated users.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            # If the user is authenticated, redirect to a different URL
            return redirect(reverse('authentication:signin'))  # Change 'home' to the desired URL name
        else:
            # If the user is not authenticated, call the original view function
            return view_func(request, *args, **kwargs)
    return wrapper_func