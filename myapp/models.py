from django.db import models
from django.utils import timezone

# Create your models here.

class roomdata(models.Model):
    rid = models.CharField(max_length=20)
    espid = models.TextField(max_length=20)
    panelid = models.TextField(max_length=20)
    ac1name = models.TextField(max_length=20)
    ac2name = models.TextField(max_length=20)
    ac1 = models.BooleanField(default=False)
    acesp = models.BooleanField(default=False)
    ac1lock = models.BooleanField(default=False)
    ac2 = models.BooleanField(default=False)
    ac2lock = models.BooleanField(default=False)
    ping = models.DateTimeField(auto_now_add=True)

class ac(models.Model):
    no = models.IntegerField()
    rid = models.CharField(max_length=20)
    espid = models.TextField(max_length=20)
    panelid = models.TextField(max_length=20)
    name = models.TextField(max_length=20)
    value = models.BooleanField(default=False)
    lock = models.BooleanField(default=False)
    ping = models.DateTimeField(auto_now_add=True)




class datalogs(models.Model):
    rid = models.CharField(max_length=20)
    ac1cur = models.FloatField()
    ac2cur = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)



class acdatalogs(models.Model):
    espid = models.CharField(max_length=20)
    no = models.IntegerField()
    accur = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
