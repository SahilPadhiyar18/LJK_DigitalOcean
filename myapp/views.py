from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.template import loader
import json
from django.core import serializers

from datetime import datetime
from django.utils import timezone

# Create your views here

# serialized_queryset = serializers.serialize('json', )


def espac(request):
    roomid = request.GET['rid']
    if roomdata.objects.filter(rid=roomid).exists():
        ac1c = request.GET['ac1']
        ac2c = request.GET['ac2']
        roomdata.objects.filter(rid = roomid).update(ping = datetime.now(tz=timezone.utc))
        datalogs(rid=roomid,ac1cur=ac1c,ac2cur=ac2c).save()
        return JsonResponse(list(roomdata.objects.all()), safe=False)
    return (HttpResponse("Sas"))

    
def home(request):
    mydata = roomdata.objects.all().order_by('rid').values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mydata,
        }
    return HttpResponse(template.render(context, request)) 

def data(request):
    mydata = datalogs.objects.all().order_by('rid').values()
    template = loader.get_template('home.html')
    context = {
        'mymembers': mydata,
        }
    return HttpResponse(template.render(context, request)) 


def cheakbox(request):
    try:
        data = json.load(request)
        roomdata.objects.filter(rid = data.get('rid') ).update(**{data.get('name'):data.get('value')})
        return HttpResponse("data")
    except:
        return HttpResponse("pass")
    
