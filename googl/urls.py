from django.urls import path,include
from .import views

urlpatterns=[
path('goog',views.goog,name='goog'),

]