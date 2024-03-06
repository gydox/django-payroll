from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.urls import reverse_lazy


app_name = "authentication"

urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("recover", views.recover, name="recover"),

]