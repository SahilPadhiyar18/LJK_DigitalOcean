from django.contrib import admin
from django.urls import path, include
from .views import home,espac

urlpatterns = [
    path("",home,name="home"),
    path("espac",espac,name="espac"),

]
