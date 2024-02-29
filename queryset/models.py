from trace import Trace
from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Emp_id = models.CharField(max_length=20,unique=True)
    mob_no = models.CharField(max_length=12)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Name}-{self.Emp_id}"

class Employee_Details(models.Model):
    Emp_Name = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
    Joining_date = models.DateField()
    Last_date = models.DateField(null=True,blank=True)

    # def __str__(self):
    #     return self.Emp_Name
