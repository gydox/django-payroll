from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FullTimeEmployeeForm, PartTimeEmployeeForm, DeleteEmployeeForm
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
def edit_employee(request, employee_id):
    try:
        employee = FullTimeEmployee.objects.get(employee_id=employee_id)
        employee_type = 'full_time'
    except FullTimeEmployee.DoesNotExist:
        try:
            employee = PartTimeEmployee.objects.get(employee_id=employee_id)
            employee_type = 'part_time'
        except PartTimeEmployee.DoesNotExist:
            messages.error(request, "Employee not found")
            raise Exception("Employee not found")

    if employee_type == 'full_time':
        form_class = FullTimeEmployeeForm
    elif employee_type == 'part_time':
        form_class = PartTimeEmployeeForm
    else:
        messages.error(request, "Employee instance missmatch error")
        pass

    if request.method == 'POST':
        if 'delete_employee' in request.POST:
            delete_form = DeleteEmployeeForm(request.POST)
            if delete_form.is_valid():
                full_name = delete_form.cleaned_data['full_name']
                if full_name == employee.full_name:  # Assuming employee has a 'full_name' field
                    employee.delete()
                    messages.success(request, 'Employee deleted successfully')
                    return redirect('employee:list')  # Redirect to a success URL after deletion
                else:
                    messages.error(request, 'Employee full name does not match')
                    return redirect('employee:edit_employee', employee_id=employee_id)
        else:
            form = form_class(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                messages.success(request, 'Employee updated')
                return redirect('employee:edit_employee', employee_id=employee_id)
            else:
                messages.error(request, form.errors)
    else:
        form = form_class(instance=employee)
    return render(request=request,
                  template_name="employee/edit_employee.html",
                  context={
                    'form': form, 
                    'employee_id': employee_id,
                    'messages': messages.get_messages(request),
                  })