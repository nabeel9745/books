from django.urls import path
from .import views

urlpatterns=[
    path('form',views.form,name='form'),
    path('crudshow',views.c_show,name='crudshow'),
    path('dele/<int:id>',views.dele,name='dele'),
    path('upd/<int:id>',views.upd,name='upd'),
    path('editing/<int:id>',views.editing,name='editing'),
    path('log',views.log,name='log'),
    path('a',views.a,name='a'),
    path('logout',views.logout,name='logout'),
    path('accepted/<int:id>',views.accepted,name='accepted'),








]