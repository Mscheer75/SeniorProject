from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from login.forms import JoinForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")



def join(request):
    if(request.method == 'POST'):
        join_form = JoinForm(request.POST)
        if(join_form.is_valid()):
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            join_form = JoinForm()
            page_data = {"join_form":join_form}
            return render(request, 'login/join.html',page_data)

    else:
        join_form = JoinForm()
        page_data = {"join_form":join_form}
        return render(request, 'login/join.html',page_data)


def user_login(request):
    if (request.method =='POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active")
            else:
                print("Someone tried to login and failed")
                print("They user username: {} and password {}".format(username,password))
                return render(request, 'login/login.html',{"login_form":LoginForm})
    else:
        return render(request, 'login/login.html',{"login_form":LoginForm})
