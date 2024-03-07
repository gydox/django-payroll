from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def employee_list(request):
    return render(request=request,
                  template_name="employee/employee_list.html",
                  context={
                  })