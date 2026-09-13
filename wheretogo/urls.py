from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.places, name='places'),
    path('add_place/', views.add_place, name='add_place'),
    path('clear/', views.clear_places, name='clear_places'),
    path('place/<int:place_id>/edit/', views.edit_place, name='edit_place'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
]
