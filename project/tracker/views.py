from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return HttpResponse('Hello')

def sighting(request):
    sightings = Sighting.objects.all()
    context = {'sighting': sightings}
    return render(request, 'tracker/sightings.html',context)
