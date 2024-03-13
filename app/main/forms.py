from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'number', 'address', 'city', 'state', 'postal_code', 'country']
        labels = {
            'name': 'Company Name',
            'number': 'Company Number',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'postal_code': 'Postal Code',
            'country': 'Country',
        }