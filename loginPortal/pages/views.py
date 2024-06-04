from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from loginApp.models import *
from loginApp.serializer import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views


#
# from django.shortcuts import render
from rest_framework import viewsets
# from .models import cbtUser
# from .serializer import loginAppSerializer
from django.http import JsonResponse, HttpResponse
from loginPortal.cbt_loginResponse_api import loginResponse
from loginPortal.constant import *
from loginPortal.connection import *
import re
from loginPortal.settings import *
import random
from django.template import loader
from django.contrib import messages
from loginApp.views import userViewSet



# HTML login Connection
def homePage(request):
    return render(request,"index.html")

def singin(request):

   
    return render(request, "login.html")
        

def singUp(request,data_id=None):
    if data_id is not None:
        data_obj = cbtUser.objects.get(user_id=data_id)
        context = {'action':'update','data_id':data_obj.user_id}
        return render(request,'singup.html',context,)

    else:
        context = {'action':'add','data_id':''}
        return render(request,'singup.html',context)

def viewCall(request,data_id=None):
        
    if data_id is not None:
        data_obj = cbtUser.objects.filter(state_active=1)       
        data_obj1 = cbtUser.objects.get(user_id=data_id)
        context = {'action':'update','data_id':data_obj1.user_id,'data_obj':data_obj}
        return render(request,'employee.html',context)

    else:
        context = {'action':'add','data_id':''}
        
    
        
    context = {'data_obj':data_obj}
    
    return render(request,'employee.html',context)
    
def singout(request):
    logout(request)
    messages.success(request,"you Logout")
    return render(request, "index.html")

def ForgetPassword(request):
    
    return render(request,"forgetpage.html")

def changePassword(request):
    return render(request,"otpfill.html")
 
