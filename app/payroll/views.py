from django.shortcuts import render, redirect, get_object_or_404
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