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
            ('Image processing for Counting and differentiating types of plants in farms','Image processing for Counting and differentiating types of plants in farms'),
            ('Utilize image processing to assess the health of plants, allowing early detection of issues before they become major problems','Utilize image processing to assess the health of plants, allowing early detection of issues before they become major problems'),
            ('Design and development of drone hardware and software systems','Design and development of drone hardware and software systems'),
            ('Path Planning for Autonomous Drones','Path Planning for Autonomous Drones'),
            ('Designing of Agricultural Spraying Drone','Designing of Agricultural Spraying Drone'),
            ('Drone-Based Lake Water Level Measurement and Analysis using Image Processing Techniques','Drone-Based Lake Water Level Measurement and Analysis using Image Processing Techniques'),
            ('Advanced Path Planning and Navigation for Drones: Techniques and Applications','Advanced Path Planning and Navigation for Drones: Techniques and Applications'),
            ('Automated Vehicle Detection and Counting using Image Processing Techniques','Automated Vehicle Detection and Counting using Image Processing Techniques'),
            ('Advanced Techniques for Inter-Communication and Coordination of Autonomous Drones in Dynamic Environments: Principles, Algorithms, and Applications', 'Advanced Techniques for Inter-Communication and Coordination of Autonomous Drones in Dynamic Environments: Principles, Algorithms, and Applications'),
            ('Advanced Techniques for 3D Mapping using Drones: Principles, Methods, and Applications','Advanced Techniques for 3D Mapping using Drones: Principles, Methods, and Applications'),
            ('Drone-Based Surveillance and Security: Techniques and Applications of Image Processing and Machine Learning','Drone-Based Surveillance and Security: Techniques and Applications of Image Processing and Machine Learning'),
            ]

genderchoice=[
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
]
institutechoice=[
         ('LJIET','LJIET'),
        ('LJ Polytechinc','LJ Polytechinc'),
        ('LJ MCA','LJ MCA'),
         ('LJ BCA','LJ BCA'),
         ('O','Others'),
]
# Create your models here.

# NEW MODELS
class RegisterUserData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    subject = models.CharField(max_length=90, choices=coursechoices, default='c1') 
    gender = models.CharField(max_length=90, choices=genderchoice, default='M')
    institute = models.CharField(max_length=90, choices=institutechoice, default='LJIT')
    
    
# class NewRegisterUserData(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     branch = models.CharField(max_length=255)
#     subject = models.CharField(max_length=90, choices=coursechoices, default='c1') 
#     gender = models.CharField(max_length=90, choices=genderchoice, default='M')
#     institute = models.CharField(max_length=90, choices=institutechoice, default='LJIT')
