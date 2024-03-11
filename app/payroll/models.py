from django.db import models
from django.db.models import UniqueConstraint

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

    class Meta:
        # Add a unique constraint to ensure no duplicate Payslip for the same month and year
        constraints = [
            UniqueConstraint(fields=['year', 'month'], name='unique_payslip_per_month_year')
        ]

    def __str__(self):
        return f"Payslip for {self.get_month_display()} {self.year}"