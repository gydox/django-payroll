from django.contrib import admin
from .models import Payroll, PayrollItem, IncomeItem, Earnings, Deductions, EarningAllocation, DeductionAllocation, EarningAllocationArchive, DeductionAllocationArchive

admin.site.register(Payroll)
admin.site.register(PayrollItem)
admin.site.register(IncomeItem)
admin.site.register(Earnings)
admin.site.register(Deductions)
admin.site.register(EarningAllocation)
admin.site.register(DeductionAllocation)
admin.site.register(EarningAllocationArchive)
admin.site.register(DeductionAllocationArchive)
