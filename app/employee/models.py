from django.db import models
from django.conf import settings


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    start_date = models.DateField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='employee/profile', blank=True, null=True)
    position = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"
    
    def photo_url(self):
        if self.photo:
            return self.photo.url
        else:
            return settings.STATIC_URL + 'assets/img/people/placeholder-avatar.png'

    def employment_type(self):
        if isinstance(self, FullTimeEmployee):
            return 'Full Time'
        elif isinstance(self, PartTimeEmployee):
            return 'Part Time'
        else:
            return 'Unknown'


class FullTimeEmployee(Employee):
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    medical_leave = models.IntegerField()
    annual_leave = models.IntegerField()

    def __str__(self):
        return f"{super().__str__()} (Full Time)"


class PartTimeEmployee(Employee):
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{super().__str__()} (Part Time)"
