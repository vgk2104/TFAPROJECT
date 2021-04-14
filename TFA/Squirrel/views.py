from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Squirrel.models import Squirrel
from Squirrel.forms import SquirrelForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Avg, Max, Min, Count

def map(request):
    sightings = list(Squirrel.objects.all())[:100]
    context = {'sightings': sightings}
    return render(request, 'Squirrel/map.html', context)


def squirrel_list(request):
    list_squirrels = list(Squirrel.objects.all())
    context = {'squirrels': list_squirrels}
    return render(request, 'Squirrel/list_squirrel.html', context)

def edit_squirrel(request, unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=unique_squirrel_id)
    if request.method == 'Post':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)
    context = {
        'form': form
    }
    return render(request, 'Squirrel/edit_squirrel.html', context)


def stats(request):
    squirrels = Squirrel.objects.all()
    total = len(squirrels)
    latitude = squirrels.aggregate(minimum=Min('Y'), maximum=Max('Y'))
    longitude = squirrels.aggregate(minimum=Min('X'), maximum=Max('X'))
    primary_fur_color = list(squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))
    Age = list(squirrels.values_list('Age').annotate(Count('Age')))
    shift = list(squirrels.values_list('Shift').annotate(Count('Shift')))
    context = {'total': total,
               'latitude': latitude,
               'longitude': longitude,
               'primary_fur_color': primary_fur_color,
               'Age': Age,
               'shift': shift,
               }
    return render(request, 'Squirrel/stats.html', context)

def add_squirrel(request):
    if request.method == 'Post':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel/')
    else:
        form = SquirrelForm()
    context = {
        'form': form
    }
    return render(request, 'Squirrel/add_squirrel.html', context)
