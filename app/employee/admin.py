from django.contrib import admin

from .models import Employee, FullTimeEmployee, PartTimeEmployee

class EmployeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(FullTimeEmployee)
admin.site.register(PartTimeEmployee)