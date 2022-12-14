from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("espac",espac,name="espac"),
    # path("delete",delete,name="delete"),
    path("cheakbox",cheakbox,name="cheakbox"),
    path("data",data,name="data"),
    path("chart",chart,name="chart"),
    path('population-chart/',population_chart, name='population-chart'),
    path('acdetails',acdetails, name='acdetails'),
    path('acupdate',acupdate, name='acupdate'),
    path('home1',home1, name='home1'),

]
