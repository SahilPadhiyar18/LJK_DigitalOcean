from django.db import models

# Create your models here.

class roomdata(models.Model):
    rid = models.CharField(max_length=20)
    espid = models.TextField(max_length=20)
    ac1 = models.BooleanField(default=False)
    ac2 = models.BooleanField(default=False)
