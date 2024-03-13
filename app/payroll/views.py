from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee.models import Employee, FullTimeEmployee, PartTimeEmployee
from .models import Payroll, PayrollItem, IncomeItem, Earnings, Deductions, EarningAllocation, DeductionAllocation, EarningAllocationArchive, DeductionAllocationArchive
from django.contrib import messages

@login_required
def payroll(request):
    return render(request=request,
                  template_name="payroll/payroll.html",
                  context={
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