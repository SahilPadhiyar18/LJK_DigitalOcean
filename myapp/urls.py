from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("espac",espac,name="espac"),
    # path("delete",delete,name="delete"),
    path("cheakbox",cheakbox,name="cheakbox"),
    path("data",data,name="data"),



]
