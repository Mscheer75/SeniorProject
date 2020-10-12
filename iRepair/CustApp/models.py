from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=30)
    address = models.CharField(max_length=30)


class Device(models.Model):
    Model_Number = models.CharField(max_length=30)
    Color = models.CharField(max_length=30)
    Device_type = models.CharField(max_length=30)
    Device_Name = models.CharField(max_length=30)
    Manufacture = models.CharField(max_length=30)

class WorkOrder(models.Model):
    Device = models.ForeignKey('Device', on_delete=models.CASCADE)
    Customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date = models.DateField()
    Employee = models.CharField(max_length=30)
    TypeRepair = models.CharField(max_length=100)
    Completed = models.BooleanField()
