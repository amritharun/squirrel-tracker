from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
        path('', views.main),
        path('map/',views.map),
        path('sightings/stats/',views.get_stats),
        path('sightings/add/',views.add_squirrel),
        path('sightings/',views.sighting),
        path('sightings/<str:S_ID>/',views.edit_squirrel),
        ]

