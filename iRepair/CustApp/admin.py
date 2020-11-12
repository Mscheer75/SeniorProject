from django.contrib import admin
from CustApp.models import Customer
from CustApp.models import Device
from CustApp.models import WorkOrder
admin.site.register(Customer)
admin.site.register(Device)
admin.site.register(WorkOrder)
# Register your models here.
