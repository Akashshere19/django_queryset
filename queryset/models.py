from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Emp_id = models.CharField(max_length=20)
    mob_no = models.CharField(max_length=12)
    Email = models.EmailField()

    def __str__(self):
        return self.Name

class Employee_Details(models.Model):
    Joining_date = models.DateField()
    Last_date = models.DateField()
