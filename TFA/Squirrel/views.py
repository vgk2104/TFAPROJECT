from django.shortcuts import render
from django.http import HttpResponse
from Squirrel.models import Squirrel


def map(request):
    squirrels = list(Squirrel.objects.all())[:100]
    context = {'squirrels': squirrels}
    return render(request, 'Squirrel/map.html', context)
