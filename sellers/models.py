from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phn=models.BigIntegerField()
    address=models.TextField(max_length=50)

class input_property(models.Model):
    p_name=models.CharField(max_length=50)
    p_address=models.CharField(max_length=50)
    p_landmark=models.CharField(max_length=50)
    P_city=models.CharField(max_length=50)
    p_state=models.CharField(max_length=10)
    p_pincode=models.BigIntegerField()

class contacts(models.Model):
    msg_name = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    replay = models.CharField(max_length=100,default='')  