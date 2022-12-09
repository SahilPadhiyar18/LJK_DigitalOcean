from django.db import models
from django.utils.timezone import now
from datetime import datetime
# Create your models here.

class roomdata(models.Model):
    rid = models.CharField(max_length=20)
    espid = models.TextField(max_length=20)
    panelid = models.TextField(max_length=20)
    ac1name = models.TextField(max_length=20)
    ac2name = models.TextField(max_length=20)
    ac1 = models.BooleanField(default=False)
    ac1lock = models.BooleanField(default=False)
    ac2 = models.BooleanField(default=False)
    ac2lock = models.BooleanField(default=False)
    ping = models.DateTimeField(default=datetime.now())

class datalogs(models.Model):
    rid = models.CharField(max_length=20)
    ac1cur = models.FloatField()
    ac2cur = models.FloatField()
    time = models.DateTimeField(default=datetime.now)
