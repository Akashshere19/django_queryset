from django.shortcuts import render

import queryset
from .models import *
# Create your views here.

def index(request):
    # emp_data = Employee.objects.all()
    # print(emp_data)
    # print("SQL Query:",emp_data.query)

    # emp_data = Employee.objects.filter(Name="Akash")
    # emp_data = Employee.objects.filter(Emp_id=14)
    # print(emp_data)
    # print("SQL Query:",emp_data.query)

    # emp_data  = Employee.objects.exclude(Emp_id =125)
    # print(emp_data)
    # print("SQL Query:",emp_data.query)

    # emp_data = Employee.objects.order_by('Name')
    # emp_data = Employee.objects.order_by('mob_no')
    # print(emp_data)
    # print("SQL Query:",emp_data.query)

    # emp_data = Employee.objects.order_by('-Name')
    # emp_data = Employee.objects.order_by('mob_no')
    # print(emp_data)
    # print("SQL Query:",emp_data.query)

    # emp_data = Employee.objects.order_by('Name').reverse()
    # emp_data = Employee.objects.order_by('?')
    # emp_data = Employee.objects.order_by('Name').reverse()[:3]
    # emp_data = Employee.objects.order_by('Name').reverse()[1:3]
    # emp_date = Employee.objects.values()
    # emp_data = Employee.objects.values('Name','Email')
    # emp_data = Employee.objects.values_list()
    # emp_data = Employee.objects.values_list('Name','Email',named=True)
    # emp_data = Employee_Details.objects.all()
    # emp_data = Employee_Details.objects.dates('Joining_date','month')
    # emp_data = Employee_Details.objects.values_list('Emp_Name','Joining_date',named=True)
    emp_data = Employee.objects.filter(Name='Akash',Email='akash@servicenet.in')
    print(emp_data)
    em_data = emp_data.union(emp_data)
    print(em_data)
    print("SQL Query:",emp_data.query)

    return render(request,'index.html',{'emp_data':emp_data})

    