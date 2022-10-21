from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class big_form(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    phn=models.BigIntegerField()
    address=models.TextField(max_length=100)
    approved = models.CharField(max_length=100, default='not approved')


    # class Meta:
    #     db_table="form_login"