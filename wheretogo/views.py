from django.shortcuts import render


def home(request):
    return render(request, 'wheretogo/home.html')


def places(request):
    return render(request, 'wheretogo/places.html')


def add_place(request):
    return render(request, 'wheretogo/add_place.html')
