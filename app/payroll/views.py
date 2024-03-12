from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee.models import Employee, FullTimeEmployee, PartTimeEmployee
from django.contrib import messages

@login_required
def payroll(request):
    return render(request=request,
                  template_name="payroll/payroll.html",
                  context={
                  })

@login_required
def history(request):
    return render(request=request,
                  template_name="payroll/history.html",
                  context={
                  })

@login_required
def payslip(request):
    return render(request=request,
                  template_name="payroll/payslip.html",
                  context={
                  })