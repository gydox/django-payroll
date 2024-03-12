from django import forms
from .models import FullTimeEmployee, PartTimeEmployee

class FullTimeEmployeeForm(forms.ModelForm):
    class Meta:
        model = FullTimeEmployee
        fields = ['employee_id', 'full_name', 'pin', 'start_date', 'email', 'phone_number', 'photo', 'position', 'active', 'monthly_salary', 'medical_leave', 'annual_leave']

class PartTimeEmployeeForm(forms.ModelForm):
    class Meta:
        model = PartTimeEmployee
        fields = ['employee_id', 'full_name', 'pin', 'start_date', 'email', 'phone_number', 'photo', 'position', 'active', 'hourly_rate']

class DeleteEmployeeForm(forms.Form):
    full_name = forms.CharField(label='Employee Full Name')