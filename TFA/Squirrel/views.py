from django.shortcuts import render
from django.http import HttpResponse

def map_(request):
    return render(request, 'Squirrel/map.html')
