"""TFA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Squirrel.views import map, squirrel_list, add_squirrel
from Squirrel.views import map, edit_squirrel, stats, index
from Squirrel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/',squirrel_list, name='sightings'),
    path('sightings/add/', add_squirrel, name='add'),
    path('sightings/<str:unique_squirrel_id>/',edit_squirrel, name = 'edit'),
    path('sightings/stats', stats, name = 'stats'),
]
