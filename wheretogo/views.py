from datetime import datetime
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

DEFAULT_PLACES = [
    {
        'id': 0,
        'name': 'ChinChin',
        'description':
            ('Ідеальне місце для поціновувачів азійської кухні! Гарний та автентичний інтер\'єр,'
             ' цікаві позиції в меню на кшталт "Капучино том ям", фісташкового sour-коктейлю та багато іншого.'
             ' Але замовлення іноді доведеться почекати довго...'),
        'type': 'Asian Cuisine Cafe',
        'location': 'Київ, Поділ',
        'rating': 4,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
    },
    {
        'id': 1,
        'name': 'Білий Налив',
        'description': 'Легендарне місце з смачнющим сидром і наливками, але народу іноді дуже багато, особливо о 22 в п\'ятницю.',
        'type': 'Bar',
        'location': 'Київ, Поштова Площа',
        'rating': 4,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
    },
    {
        'id': 2,
        'name': 'FluRanet',
        'description': 'Дуже цікавий магазин з дуже цікавим асортиментом 👀. Обережно! В середині може стати зле!',
        'type': 'Craft Supplies Store',
        'location': 'Київ, Андріївський узвіз',
        'rating': 5,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
]


def get_session_places(request):
    if 'places_list' not in request.session:
        request.session['places_list'] = list(DEFAULT_PLACES)
        request.session.modified = True
    return request.session['places_list']


def home(request):
    places_list = get_session_places(request)
    return render(request, 'wheretogo/home.html', {'places': places_list})


def places(request):
    places_list = request.session.get('places_list', [])
    return render(request, 'wheretogo/places.html', {'places': places_list})


def add_place(request):
    if request.method == 'POST':
        places_list = get_session_places(request)
        name = request.POST.get('name')
        description = request.POST.get('description')
        place_type = request.POST.get('type')
        location = request.POST.get('location')
        rating = request.POST.get('rating')
        if not name:
            return render(request, 'wheretogo/add_place.html', {'error': 'Name of the place cannot be empty!'})
        if any(place.get('name') == name for place in places_list):
            return render(request, 'wheretogo/add_place.html', {'error': 'This place has already been added!'})

        new_place = {
            'id': len(places_list),
            'name': name,
            'description': description,
            'type': place_type,
            'location': location,
            'rating': int(rating) if rating else None,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        places_list.append(new_place)
        request.session['places_list'] = places_list
        request.session.modified = True
        return redirect('places')
    return render(request, 'wheretogo/add_place.html')


def edit_place(request, place_id):
    places_list = get_session_places(request)
    place = next((p for p in places_list if p.get('id') == place_id), None)
    if not place:
        raise Http404("There is no such place...")
    if request.method == 'POST':
        name = request.POST.get('name')
        place['description'] = request.POST.get('description')
        place['type'] = request.POST.get('type')
        place['location'] = request.POST.get('location')
        rating = request.POST.get('rating')
        place['name'] = name
        if rating:
            place['rating'] = int(rating)
        if not name:
            return render(request, 'wheretogo/edit_place.html', {'place': place, 'error': 'Name of the place cannot be empty!'})
        if any(p.get('name').lower() == name.lower() and p.get('id') != place_id for p in places_list):
            return render(request, 'wheretogo/edit_place.html', {'place': place, 'error': 'Place with this name already exists'})
        request.session.modified = True
        messages.success(request, 'Changes saved successfully!')
        return redirect('edit_place', place_id=place['id'])
    return render(request, 'wheretogo/edit_place.html', {'place': place, })


def clear_places(request):
    request.session.pop('places_list', None)
    request.session.modified = True
    return redirect('places')


def place_detail(request, place_id):
    places_list = request.session.get('places_list', [])
    place = next((p for p in places_list if p.get('id') == place_id), None)
    if not place:
        return redirect('places')
    return render(request, 'wheretogo/place_detail.html', {'place': place})
