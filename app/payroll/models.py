from django.db import models
from django.db.models import UniqueConstraint
from django.conf import settings
from employee.models import Employee


class Payroll(models.Model):
    YEAR_CHOICES = [
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026')
    ]

    MONTH_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    ]

    year = models.IntegerField(choices=YEAR_CHOICES)
    month = models.IntegerField(choices=MONTH_CHOICES)
    creation_date = models.DateField(auto_now_add=True)
    processed = models.BooleanField(default=False)


    class Meta:
        # Add a unique constraint to ensure no duplicate Payslip for the same month and year
        constraints = [
            UniqueConstraint(fields=['year', 'month'], name='unique_payslip_per_month_year')
        ]

    def __str__(self):
        return f"Payslip for {self.get_month_display()} {self.year}"

    def get_month_name(month_number):
        for month_tuple in Payroll.MONTH_CHOICES:
            if month_tuple[0] == month_number:
                return month_tuple[1]
        return None  # Return None if month_number is invalid

    @property
    def total_amount(self):
        return sum(item.amount for item in self.payroll_information.all())

class PayrollItem(models.Model):
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE, related_name='payroll_information')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)    

    def __str__(self):
        return f"Salary information for {self.employee} in {self.payroll.get_month_display()} {self.payroll.year}"


class IncomeItem(models.Model):
    epf = models.BooleanField(default=False)
    socso = models.BooleanField(default=False)
    eis = models.BooleanField(default=False)
    irbm = models.BooleanField(default=False)
    hrdcorp = models.BooleanField(default=False)

class Earnings(IncomeItem):
    name = models.CharField(max_length=100)

class Deductions(IncomeItem):
    name = models.CharField(max_length=100)


class EarningAllocation(models.Model):
    name = models.ForeignKey(Earnings, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class DeductionAllocation(models.Model):
    name = models.ForeignKey(Deductions, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class EarningAllocationArchive(models.Model):
    payroll_item = models.ForeignKey(PayrollItem, on_delete=models.CASCADE, related_name='earning_allocations_archive')
    name = models.CharField(max_length=100)  # Directly store the name
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class DeductionAllocationArchive(models.Model):
    payroll_item = models.ForeignKey(PayrollItem, on_delete=models.CASCADE, related_name='deduction_allocations_archive')
    name = models.CharField(max_length=100)  # Directly store the name
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

