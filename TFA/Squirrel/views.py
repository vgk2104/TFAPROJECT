from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Squirrel.models import Squirrel
from Squirrel.forms import SquirrelForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

def map(request):
    squirrels = list(Squirrel.objects.all())[:100]
    context = {'squirrels': squirrels}
    return render(request, 'Squirrel/map.html', context)


def squirrel_list(request):
    list_squirrels = list(Squirrel.objects.all())
    context = {'squirrels': list_squirrels}
    return render(request, 'Squirrel/list_squirrel.html', context)


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
