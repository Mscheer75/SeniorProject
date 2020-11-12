from django.shortcuts import render
from django.http import HttpResponse
from CustApp.forms import customerForm
from CustApp.forms import deviceForm
from CustApp.forms import workForm
from CustApp.models import Customer
from CustApp.models import Device
from CustApp.models import WorkOrder
from CustApp.models import pageSettings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.


@login_required(login_url='/login/')
def cust(request):

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



@login_required(login_url='/login/')
def data(request):
    page_data= {"completed":0, "NotCompleted":0}

    comp = 0
    ncomp = 0
    workList = WorkOrder.objects.all()
    for item in workList:
        if(item.Completed == True):
            comp += 1
        else:
            ncomp +=1

    page_data["completed"] = comp
    page_data["NotCompleted"] = ncomp

    return render(request, 'CustApp/data.html', page_data)



@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def flip(request, id):
    temp = WorkOrder.objects.get(id=id)
    if(temp.Completed == True):
        temp.Completed = False
    else:
        temp.Completed = True
    temp.save()
    return redirect(WorkOrderView)


@login_required(login_url='/login/')
def flippick(request, id):
    temp = WorkOrder.objects.get(id=id)
    if(temp.PickedUp == True):
        temp.PickedUp = False
    else:
        temp.PickedUp = True
    temp.save()
    return redirect(WorkOrderView)

@login_required(login_url='/login/')
def WorkOrderView(request):
     #print("taskuser:",request.user)

    user = request.user
    if(pageSettings.objects.filter(user=user).exists()):
        userProf = pageSettings.objects.get(user=user)
    else:
        user_profile = pageSettings();
        user_profile.user = user
        user_profile.save()

    userProf = pageSettings.objects.get(user=user)

    page_data = {"dev_form":deviceForm, "cust_form":customerForm, "work_form":workForm,"workDict":[], "toggleHeader":""}
    work_form = workForm(request.POST);
    cust_form = customerForm(request.POST);
    dev_form = deviceForm(request.POST);
    user = request.user

    if(request.method == 'POST'):
        print("true")
        if(work_form.is_valid() and cust_form.is_valid() and dev_form.is_valid()):
            Device_Name = dev_form.cleaned_data["Device_Name"]
            Model_Number = dev_form.cleaned_data["Model_Number"]
            Color= dev_form.cleaned_data["Color"]
            Device_type = dev_form.cleaned_data["Device_type"]
            Manufacture = dev_form.cleaned_data["Manufacture"]

            if (Device.objects.filter(Color=Color, Device_Name=Device_Name, Model_Number=Model_Number, Device_type=Device_type).exists()):
                print("Object exsits")
            else:
                Device(Device_Name=Device_Name, Color=Color, Device_type=Device_type, Model_Number=Model_Number, Manufacture=Manufacture).save()
                #print("created new Object")

            CustDevice = Device.objects.filter(Device_Name=Device_Name, Color=Color, Device_type=Device_type, Model_Number=Model_Number, Manufacture=Manufacture)


            first_name = cust_form.cleaned_data["first_Name"]
            last_name = cust_form.cleaned_data["last_Name"]
            phone_Number= cust_form.cleaned_data["phone_Number"]
            address = cust_form.cleaned_data["address"]

            if (Customer.objects.filter(first_name=first_name, last_name=last_name, phoneNumber=phone_Number).exists()):
                print("Object exsits")
            else:
                Customer(first_name=first_name, last_name=last_name, phoneNumber=phone_Number, address=address).save()
                #print("created new Object")

            CustPerson = Customer.objects.filter(first_name=first_name, last_name=last_name, phoneNumber=phone_Number)

            TypeRepair= work_form.cleaned_data["TypeRepair"]

            WorkOrder(DeviceRepair=CustDevice[0], CustomerRepair=CustPerson[0], TypeRepair=TypeRepair, user=user, Completed=False, PickedUp=False).save()
        else:
            page_data["work_form"]=work_form




    workEverything = WorkOrder.objects.all()

    for row_num in range(len(workEverything)):
        row = {}
        record = workEverything[row_num]

        id = record.id
        CustomerRepairFirst = record.CustomerRepair.first_name
        CustomerRepairLast = record.CustomerRepair.last_name
        CustomerNumber = record.CustomerRepair.phoneNumber
        DeviceRepairName = record.DeviceRepair.Device_Name
        TypeRepair = record.TypeRepair
        Completed = record.Completed
        PickedUp = record.PickedUp


        Completed = 'No'
        if( record.Completed == True):
            Completed = 'Yes'
        else:
            Completed = 'No'

        PickedUp = 'No'
        if( record.PickedUp == True):
            PickedUp = 'Yes'
        else:
            PickedUp = 'No'

        date = record.date
        user = record.user

        row['id']=record.id
        row[CustomerRepairFirst]=record.CustomerRepair.first_name
        row[CustomerRepairLast]=record.CustomerRepair.last_name
        row[CustomerNumber]=record.CustomerRepair.phoneNumber
        row[date] = record.date
        row[DeviceRepairName]=record.DeviceRepair.Device_Name
        row[TypeRepair] = record.TypeRepair
        row['Completed'] = Completed
        row['PickedUp'] = PickedUp
        row[user] = record.user
        page_data["toggleHeader"] = "All Work orders"
        if(userProf.profile_setting_1 == False and userProf.profile_setting_2 == False):
            page_data.get("workDict").append(row)
            page_data["toggleHeader"] = "All Work orders"
        elif((userProf.profile_setting_1 == True and record.Completed == False) and userProf.profile_setting_2 == False):
            page_data.get("workDict").append(row)
            page_data["toggleHeader"] = "Work Orders that are not Completed"
        elif((userProf.profile_setting_2 == True and record.PickedUp == False) and userProf.profile_setting_1 == False):
            page_data.get("workDict").append(row)
            page_data["toggleHeader"] = "Work Orders that have not been picked Up"
        elif((userProf.profile_setting_1 == True and record.Completed == False) and (userProf.profile_setting_2 == True and record.PickedUp == False)):
            page_data.get("workDict").append(row)
            page_data["toggleHeader"] = "Work Orders that have not been Completed and have not been Picked Up"
    print(page_data["toggleHeader"])
    return render(request, 'CustApp/WorkOrder.html', page_data)



@login_required(login_url='/login/')
def completeTog(request):
    user = request.user

    userProf = pageSettings.objects.get(user=user)

    if(userProf.profile_setting_1 == True):
        userProf.profile_setting_1 = False
    else:
        userProf.profile_setting_1 = True

    userProf.save()

    return redirect(WorkOrderView)

@login_required(login_url='/login/')
def pickTog(request):

    user = request.user

    userProf = pageSettings.objects.get(user=user)

    if(userProf.profile_setting_2 == True):
        userProf.profile_setting_2 = False
    else:
        userProf.profile_setting_2 = True

    userProf.save()

    return redirect(WorkOrderView)
