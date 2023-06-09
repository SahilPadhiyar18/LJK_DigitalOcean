"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myapp.urls")),
    path('espac', include("myapp.urls")),
    path('delete', include("myapp.urls")),
    path('cheakbox', include("myapp.urls")),
    # path('home', include("myapp.urls")),
    path('chart', include("myapp.urls")),
    path('population', include("myapp.urls")),
    path('acdetails', include("myapp.urls")),
    path('acupdate', include("myapp.urls")),
    path('get_data', include("myapp.urls")),
    path('waterlevelupdate', include("myapp.urls")),
    # path('',include('droneapp.urls')),
    # path('c1/',include('droneapp.urls')),
    # path('c2/',include('droneapp.urls')),
    # path('c3/',include('droneapp.urls')),
    # path('c4/',include('droneapp.urls')),
    # path('c5/',include('droneapp.urls')),
    # path('register/',include('droneapp.urls')),
]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
