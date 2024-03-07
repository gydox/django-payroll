from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.employee_id})"


class FullTimeEmployee(Employee):
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{super().__str__()} (Full Time)"


class PartTimeEmployee(Employee):
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{super().__str__()} (Part Time)"
