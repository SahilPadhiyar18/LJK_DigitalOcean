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
               ('c6','Drone-Based Lake Water Level Measurement and Analysis using Image Processing Techniques');
               ('c7','Advanced Path Planning and Navigation for Drones: Techniques and Applications'),
               ('c8','Drone-Based Surveillance and Security: Techniques and Applications of Image Processing and Machine Learning')
               ('c9','Advanced Techniques for Inter-Communication and Coordination of Autonomous Drones in Dynamic Environments: Principles, Algorithms, and Applications'),
               ('c10','Advanced Techniques for 3D Mapping using Drones: Principles, Methods, and Applications'),
               ('c11','Drone-Based Surveillance and Security: Techniques and Applications of Image Processing and Machine Learning'),
               ]
genderchoice=[
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
]

institutechoice=[
         ('LJIT','LJIT'),
        ('Polytechinc','LJ Polytechinc'),
        ('MCA','LJ MCA'),
         ('BCA','LJ BCA'),
         ('Others','Others'),
]

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
     branch= models.DateField(max_length=8)
    subject = models.CharField(max_length=90, choices=coursechoices,default='c1') 
    gender = models.CharField(max_length=90, choices=genderchoice,default='M') 
    institute = models.CharField(max_length=90, choices=institutechoice,default='Others') 
