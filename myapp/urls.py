from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("homeadms",home,name="home"),
    path("espac",espac,name="espac"),
    # path("delete",delete,name="delete"),
    path("cheakbox",cheakbox,name="cheakbox"),
    path("data",data,name="data"),
    path("chart",chart,name="chart"),
    path('population-chart/',population_chart, name='population-chart'),
    path('acdetails',acdetails, name='acdetails'),
    path('acupdate',acupdate, name='acupdate'),
    path('get_data',get_data, name='get_data'),


    path('', index, name='dronehome'),
    path('c1', c1, name="c1"),
    path('c2', c2, name="c2"),
    path('c3', c3, name="c3"),
    path('c4', c4, name="c4"),
    path('c5', c5, name="c5"),
    path('c6', c6, name="c6"),
    path('c7', c7, name="c7"),
    path('c8', c8, name="c8"),
    path('c9', c9, name="c9"),


    path('register', register, name="register"),

]
