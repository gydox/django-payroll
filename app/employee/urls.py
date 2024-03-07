from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.urls import reverse_lazy


app_name = "employee"

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
]