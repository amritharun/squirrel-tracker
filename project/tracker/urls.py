from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
        path('', views.main),
        path('sightings/stats/',views.get_stats),
        ]

