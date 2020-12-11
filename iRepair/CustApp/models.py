from django.db import models
from django.contrib.auth.models import User

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
    DeviceRepair = models.ForeignKey('Device', on_delete=models.CASCADE)
    CustomerRepair = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TypeRepair = models.CharField(max_length=100)
    Completed = models.BooleanField()
    PickedUp = models.BooleanField()

class pageSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_setting_1 = models.BooleanField(default=False)
    profile_setting_2 = models.BooleanField(default=False)
