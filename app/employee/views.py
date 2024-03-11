from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FullTimeEmployeeForm, PartTimeEmployeeForm
from .models import Employee, FullTimeEmployee, PartTimeEmployee
from django.contrib import messages


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    full_time_form = FullTimeEmployeeForm()
    part_time_form = PartTimeEmployeeForm()
    if request.method == 'POST':
        if 'full_time_submit' in request.POST:
            full_time_form = FullTimeEmployeeForm(request.POST, request.FILES)
            if full_time_form.is_valid():
                full_time_form.save()
                messages.success(request, 'Full Time Employee Created')
                return redirect('employee:full_time_employees')
            else:
                messages.error(request, full_time_form.errors)

        elif 'part_time_submit' in request.POST:
            part_time_form = PartTimeEmployeeForm(request.POST, request.FILES)
            if part_time_form.is_valid():
                part_time_form.save()
                return redirect('employee:part_time_employees')
    else:
        full_time_form = FullTimeEmployeeForm()
        part_time_form = PartTimeEmployeeForm()

    return render(request=request,
                  template_name="employee/employee_list.html",
                  context={
                        'full_time_form': full_time_form,
                        'part_time_form': part_time_form,
                        'employees': employees,
                        'messages': messages.get_messages(request),
                  })

def full_time_employees(request):
    full_time_employees = FullTimeEmployee.objects.all()
    full_time_form = FullTimeEmployeeForm()
    part_time_form = PartTimeEmployeeForm()
    if request.method == 'POST':
        if 'full_time_submit' in request.POST:
            full_time_form = FullTimeEmployeeForm(request.POST, request.FILES)
            if full_time_form.is_valid():
                full_time_form.save()
                messages.success(request, 'Full Time Employee Created')
                return redirect('employee:full_time_employees')
            else:
                messages.error(request, full_time_form.errors)

                print("form not valid")
                print(full_time_form.errors)

        elif 'part_time_submit' in request.POST:
            full_time_form = FullTimeEmployeeForm(request.POST, request.FILES)
            if part_time_form.is_valid():
                part_time_form.save()
                return redirect('employee:part_time_employees')
    else:
        full_time_form = FullTimeEmployeeForm()
        part_time_form = PartTimeEmployeeForm()

    return render(request=request,
                  template_name="employee/full_time_employees.html",
                  context={
                        'full_time_form': full_time_form,
                        'part_time_form': part_time_form,
                        'full_time_employees': full_time_employees,
                        'messages': messages.get_messages(request),

                  })

def part_time_employees(request):
    full_time_employees = PartTimeEmployee.objects.all()
    full_time_form = FullTimeEmployeeForm()
    part_time_form = PartTimeEmployeeForm()
    if request.method == 'POST':
        if 'full_time_submit' in request.POST:
            full_time_form = FullTimeEmployeeForm(request.POST, request.FILES)
            if full_time_form.is_valid():
                full_time_form.save()
                return redirect('employee:full_time_employees')
            print("form not valid")
            print(full_time_form.errors)
        elif 'part_time_submit' in request.POST:
            full_time_form = FullTimeEmployeeForm(request.POST, request.FILES)
            if part_time_form.is_valid():
                part_time_form.save()
                return redirect('employee:part_time_employees')
    else:
        full_time_form = FullTimeEmployeeForm()
        part_time_form = PartTimeEmployeeForm()

    return render(request=request,
                  template_name="employee/part_time_employees.html",
                  context={
                        'full_time_form': full_time_form,
                        'part_time_form': part_time_form,
                        'part_time_employees': full_time_employees,
                  })

@login_required
def edit_employee(request):
    return render(request=request,
                  template_name="employee/edit_employee.html",
                  context={
                  })