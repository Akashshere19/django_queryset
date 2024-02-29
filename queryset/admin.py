from pyexpat import model
from django.contrib import admin
from .models import Employee,Employee_Details
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Name','Emp_id']
     
class Employee_DetailsAdmin(admin.ModelAdmin):
    list_display = ['Emp_Name','Joining_date','Last_date']


admin.site.register(Employee,EmployeeAdmin)

admin.site.register(Employee_Details,Employee_DetailsAdmin)