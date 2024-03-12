from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.urls import reverse_lazy


app_name = "payroll"

urlpatterns = [
    path('', views.payroll, name='payroll'),
    path('payslip', views.payslip, name='payslip'),
    path('history', views.history, name='history'),
]