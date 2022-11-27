from django.shortcuts import render
from django.contrib import admin



# Create your views here.

def a_login(req):
    return render(req,'pages/admin_login.html')

