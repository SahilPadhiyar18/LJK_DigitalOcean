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


# def data(request):
#     if request.method =='POST':
#         data = request.POST['no']
#         name = request.POST['name']
#         print(request.POST['endTime'])
#         start_date=request.POST['startTime']
#         end_date=request.POST['endTime']
#         mydata = acdatalogs.objects.filter(espid=name , no=data,time__range=[start_date,end_date]).order_by('-id') .values()
#         template = loader.get_template('graph.html')
#         context = {
#             'mymembers': mydata,
#         }
#         return HttpResponse(template.render(context, request)) 
#     else:
#         mydata = acdatalogs.objects.all().distinct("espid").values()
#         template = loader.get_template('graph.html')
#         print("abd")
#         context = {
#             'mymembers': mydata,
#             }
#         return HttpResponse(template.render(context, request)) 
    
# @csrf_exempt
# def get_data(request,*args,**kwargs):
#     Data = json.load(request)
#     current = []
#     time = []
#     data = Data.get('no')
#     name = Data.get('name')
#     start_date = Data.get('startTime')
#     end_date = Data.get('endTime')
#     for i in  acdatalogs.objects.filter(espid=name , no=data,time__range=[start_date,end_date]).order_by('-id') .values():
#         current.append(i['accur'])
#         time.append(i['time'])
#     data = {
#         "current" : current,
#         "time" : time,
#     }
#     return JsonResponse(data)

@csrf_exempt
def cheakbox(request):
    try:
        data = json.load(request)
        ac.objects.filter(espid = data.get('espid') , no = data.get('no')).update(**{data.get('name'):data.get('value')})
        return JsonResponse({'foo':'bar'})
    except:
        return JsonResponse("pass")
    
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
        try:            
            acdatalogs(espid=esp32id,no=1,accur=request.GET['ac1cur']).save()
            acdatalogs(espid=esp32id,no=2,accur=request.GET['ac2cur']).save()
            acdatalogs(espid=esp32id,no=3,accur=request.GET['ac3cur']).save()
            if( ac.objects.filter(espid=esp32id,no=1).exists()):
                ac.objects.filter(espid = esp32id,no=1).update(acesp = int(request.GET['ac1']),ping = datetime.now(tz=timezone.utc))
            if( ac.objects.filter(espid=esp32id,no=2).exists()):
                ac.objects.filter(espid = esp32id,no=2).update(acesp = int(request.GET['ac2']),ping = datetime.now(tz=timezone.utc))
            if( ac.objects.filter(espid=esp32id,no=3).exists()):
                ac.objects.filter(espid = esp32id,no=3).update(acesp = int(request.GET['ac3']),ping = datetime.now(tz=timezone.utc))
            print("try done")
        except:
            print("pass")
            pass
        return JsonResponse(list(ac.objects.filter(espid=esp32id).values('no','value')), safe=False)
    # return JsonResponse(list(ac.objects.all().values('','value')), safe=False)
    # # else:    
    # return (HttpResponse("Sas"))  

    
    
    
@csrf_exempt
def get_data(request,*args,**kwargs):
    Data = json.load(request)
    current = []
    time = []
    RID = []
    index = 0
    Dname = Data.get('name')
    start_date = Data.get('startTime')
    end_date = Data.get('endTime')
    print("dname",Dname)
    data = ac.objects.filter(name = Dname).values() 
    # for i in data:
    #     print(i["rid"])
    for i in data:
        index += 1
        print("index",index)
        for j in  acdatalogs.objects.filter(espid =i['espid'] , no=i['no'],time__range=[start_date,end_date]).order_by('-id') .values():
            current.append(j['accur'])
            time.append(j['time'])
            RID.append(index)
    data = {
        "current" : current,
        "time" : time,
        "rid" : RID,
    }
    return JsonResponse(data)

def chart(request):  
    if request.method =='POST':
        data = request.POST['no']
        name = request.POST['name']
        print(request.POST['endTime'])
        start_date=request.POST['startTime']
        end_date=request.POST['endTime']
        mydata = acdatalogs.objects.filter(espid=name , no=data,time__range=[start_date,end_date]).order_by('-id') .values()
        template = loader.get_template('graph.html')
        context = {
            'mymembers': mydata,
        }
        return HttpResponse(template.render(context, request)) 
    else:
        data = []
        mydata = ac.objects.filter().values('name','espid').distinct('name')
        for i in mydata:
            # print()
            if "/" not in i['name']:
                data.append(i) 

        # print(data)
        template = loader.get_template('graph.html')
        # print("abd")
        context = {
            'mymembers': data,
            }
        return HttpResponse(template.render(context, request)) 


