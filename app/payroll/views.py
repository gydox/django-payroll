from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from employee.models import Employee, FullTimeEmployee, PartTimeEmployee
from .models import Payroll, PayrollItem, IncomeItem, Earnings, Deductions, EarningAllocation, DeductionAllocation, EarningAllocationArchive, DeductionAllocationArchive
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver

@login_required
def payroll(request):
    return render(request=request,
                  template_name="payroll/payroll.html",
                  context={
                  })

@login_required
def payroll_view(request, payroll_id):
    payroll = get_object_or_404(Payroll, pk=payroll_id)
    return render(request=request,
                  template_name="payroll/payroll_view.html",
                  context={
                    'payroll': payroll,
                  })

@login_required
def history(request):
    payrolls = Payroll.objects.all()

    return render(request=request,
                  template_name="payroll/history.html",
                  context={
                    'payrolls': payrolls,
                  })

@login_required
def payslip(request):
    return render(request=request,
                  template_name="payroll/payslip.html",
                  context={
                  })

@receiver(post_save, sender=Payroll)
def create_payroll_items(sender, instance, created, **kwargs):
    """
    Signal receiver function to create PayrollItem instances for active employees
    when a Payroll is created.
    """
    if created:
        active_employees = Employee.objects.filter(active=True)
        for employee in active_employees:
            PayrollItem.objects.create(payroll=instance, employee=employee, amount=0.0)