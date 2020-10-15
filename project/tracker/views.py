from django.shortcuts import render, redirect
from django.http import HttpResponse 

from .models import Sighting


def main(request):
    return render(request, 'tracker/main.html')

def get_stats(request):
    AM = 0
    PM = 0
    G = 0
    C = 0
    B = 0
    for m in Sighting.objects.all():
        if m.SHIFT == 'AM':
            AM += 1
        if m.SHIFT == 'PM':
            PM += 1
        if m.COLOR == 'Grey':
            G += 1
        if m.COLOR == 'Cinnamon':
            C += 1
        if m.COLOR == 'Black':
            B += 1
    context = {
	'AM':AM,
	'PM':PM,
	'G':G,
	'C':C,
	'B':B,
	}
    return render(request, 'tracker/stats.html', context)

def sighting(request):
    sightings = Sighting.objects.all()
    context = {'sighting': sightings}
    return render(request, 'tracker/sightings.html',context)
