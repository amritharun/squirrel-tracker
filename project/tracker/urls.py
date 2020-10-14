from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
        path('', views.main),
        path('sighting/stats/', views.get_stats),
        ]

