from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.places, name='places'),
    path('add_place/', views.add_place, name='add_place')
]
