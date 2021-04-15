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


def view_data(request, unique_squirrel_id):
    views = list(Squirrel_data.objects.filter(Unique_Squirrel_ID=unique_squirrel_id).values())
    return render(request, "Squirrel/view.html", {'views': views})


def stats(request):
    squirrels = Squirrel.objects.all().count()
    age_juvenile = Squirrel.objects.filter(Age='Juvenile').count()
    age_adult = Squirrel.objects.filter(Age='Adult').count()
    location_above = Squirrel.objects.filter(Location='Above Ground').count()
    location_plane = Squirrel.objects.filter(Location='Ground Plane').count()
    shift_choices_am = Squirrel.objects.filter(Shift='AM').count()
    shift_choices_pm = Squirrel.objects.filter(Shift='PM').count()
    color_choices_gray = Squirrel.objects.filter(Primary_Fur_Color='Gray').count()
    color_choices_black = Squirrel.objects.filter(Primary_Fur_Color='Black').count()
    color_choices_cinnamon = Squirrel.objects.filter(Primary_Fur_Color='Cinnamon').count()
    context = {
        'squirrels': squirrels,
        'age_juvenile': age_juvenile,
        'age_adult': age_adult,
        'location_above': location_above,
        'location_plane': location_plane,
        'shift_choices_am': shift_choices_am,
        'shift_choices_pm': shift_choices_pm,
        'color_choices_gray': color_choices_gray,
        'color_choices_black': color_choices_black,
        'color_choices_cinnamon': color_choices_cinnamon,
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
