from django.shortcuts import render
from django.http import HttpResponse
from CustApp.forms import customerForm
from CustApp.forms import deviceForm
from CustApp.models import Customer
from CustApp.models import Device
# Create your views here.



def home(request):

    page_data = { "cust_form":customerForm}

    if(request.method == 'POST' and 'custSubmit' in request.POST):
        cust_form = customerForm(request.POST);
        if(cust_form.is_valid()):
            first_Name = cust_form.cleaned_data["first_Name"]
            last_Name = cust_form.cleaned_data["last_Name"]
            phone_Number= cust_form.cleaned_data["phone_Number"]
            address = cust_form.cleaned_data["address"]

            Customer(first_name=first_Name, last_name=last_Name, phoneNumber=phone_Number, address=address).save()
        else:
            page_data["cust_form"]=cust_form


    return render(request, 'CustApp/home.html', page_data)


def data(request):
    return render(request, 'CustApp/data.html')

def device(request):

    page_data = { "dev_form":deviceForm}

    if(request.method == 'POST' and 'deviceSubmit' in request.POST):
        dev_form = deviceForm(request.POST);
        if(dev_form.is_valid()):
            Device_Name = dev_form.cleaned_data["Device_Name"]
            Model_Number = dev_form.cleaned_data["Model_Number"]
            Color= dev_form.cleaned_data["Color"]
            Device_type = dev_form.cleaned_data["Device_type"]
            Manufacture = dev_form.cleaned_data["Manufacture"]

            Device(Device_Name=Device_Name, Color=Color, Device_type=Device_type, Model_Number=Model_Number, Manufacture=Manufacture).save()
        else:
            dev_data["dev_form"]=dev_form


    return render(request, 'CustApp/device.html', page_data)

def WorkOrder(request):
    return render(request, 'CustApp/WorkOrder.html')
