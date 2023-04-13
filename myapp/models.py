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
    acesp = models.BooleanField(default=False)
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


coursechoices=[ 
               ('c1','Design and development of drone hardware and software systems'),
               ('c2','Flight testing and data collection'),
               ('c3','Algorithm development and optimization for image processing and navigation'),
               ('c4','Integration of drone systems with other technologies such as GIS, wireless communication, and cloud computing'),
               ('c5','Project management and coordination'),
               ]
genderchoice=[
    ('M','Male'),
    ('F','Female'),
]
# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday= models.DateField(max_length=8)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=90, choices=coursechoices,default='c1') 
    gender = models.CharField(max_length=90, choices=genderchoice,default='M') 