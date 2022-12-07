from django.shortcuts import render
from django.http import HttpResponse
from .models import roomdata
from django.contrib.auth.models import User, auth
from django.template import loader
# Create your views here.

def espac(request):
    a = roomdata(rid='ljp206', espid = 'ljp206',ac1=True,ac2=True)
    a.save()
#     df = roomdata.objects.all().values()
#     print("df",df)
    return HttpResponse("ok")

def home(request):
    mydata = roomdata.objects.all()
    template = loader.get_template('home.html')
    context = {
        'mymembers': mydata,
        }
    return HttpResponse(template.render(context, request)) 
    
