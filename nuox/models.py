from django.db import models

# Create your models here.

class nuox_sign(models.Model):
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)

class staff(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    password = models.TextField(max_length=100,unique=True)


class items(models.Model):
    product_name=models.CharField(max_length=100)
    rate=models.BigIntegerField()
    description=models.TextField(max_length=200)
    approved = models.CharField(max_length=100,default='not approved')