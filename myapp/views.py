from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.template import loader
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
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
        # return JsonResponse(list(roomdata.objects.filter(rid = roomid).values('ac1','ac2')), safe=False)
        return JsonResponse(list(roomdata.objects.filter(rid=roomid).values()), safe=False)
    return (HttpResponse("Sas"))

    
# def home(request):
#     mydata = ac.objects.all().order_by('id').values()
#     template = loader.get_template('index.html')
#     context = {
#         'mymembers': mydata,
#         }
#     return HttpResponse(template.render(context, request)) 

def home(request):
    mydata = ac.objects.all().order_by('id').values()
    template = loader.get_template('new.html')
    context = {
        'mymembers': mydata,
        }
    return HttpResponse(template.render(context, request)) 


def data(request):
    mydata = datalogs.objects.all().order_by('id').values()
    template = loader.get_template('home.html')
    context = {
        'mymembers': mydata,
        }
    return HttpResponse(template.render(context, request)) 

@csrf_exempt
def cheakbox(request):
    try:
        data = json.load(request)
        ac.objects.filter(espid = data.get('espid') , no = data.get('no')).update(**{data.get('name'):data.get('value')})
        return HttpResponse("data")
    except:
        return HttpResponse("pass")
    
def chart(request):
    labels = []
    data = []
    queryset = datalogs.objects.all()
    for person in queryset:
        labels.append(person.rid)
        data.append(person.ac2cur)

    return render(request,'data.html',{
        'labels':labels,
        'data':data
    }) 

def population_chart(request):
    labels = []
    data = []
    queryset = datalogs.objects.all()
    for person in queryset:
        print(person.time)
        labels.append(person.time)
        data.append(person.ac2cur)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def acdetails(request):
    try:
        esp32id = request.GET['espid']
        # print("A")
        if ac.objects.filter(espid=esp32id).exists():
            data = 0 
            for i in ac.objects.filter(espid=esp32id).values('no'):
                data = data*10 + i['no']
            return HttpResponse(data)
        else:
            return HttpResponse("Name Not Found")
    except: 
        return HttpResponse("error 404")

def acupdate(request):
    if ac.objects.filter(espid=request.GET['espid']).exists():
        esp32id = request.GET['espid']
        return JsonResponse(list(ac.objects.filter(espid=esp32id).values('no','value')), safe=False)
    # return JsonResponse(list(ac.objects.all().values('','value')), safe=False)
    # # else:    
    # return (HttpResponse("Sas"))  
