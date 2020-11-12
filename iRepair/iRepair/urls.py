"""iRepair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CustApp import views as CustApp_views
from login import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'cust/', CustApp_views.cust, name='cust'),
    path(r'device/', CustApp_views.device, name='device'),
    path(r'data/', CustApp_views.data, name='data'),
    path('', CustApp_views.WorkOrderView, name='WorkOrder'),
    path('flip/<int:id>/',CustApp_views.flip, name='flip'),
    path('flippick/<int:id>/',CustApp_views.flippick, name='flippick'),
    path(r'join/',login_views.join, name='join'),
    path(r'completeTog/', CustApp_views.completeTog, name='completeTog'),
    path(r'pickTog/', CustApp_views.pickTog, name='pickTog'),
    path(r'login/',login_views.user_login, name='user_login'),
    path(r'logout/',login_views.user_logout, name='user_logout')
]
