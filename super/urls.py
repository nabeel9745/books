from django.urls import path,include
from .import views

urlpatterns=[
    path('a_login',views.a_login,name='a_login'),

]
