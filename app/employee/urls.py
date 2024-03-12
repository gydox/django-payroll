from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.urls import reverse_lazy


app_name = "employee"

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('full_time', views.full_time_employees, name='full_time_employees'),
    path('part_time', views.part_time_employees, name='part_time_employees'),
    path('edit/<str:employee_id>', views.edit_employee, name='edit_employee'),
]