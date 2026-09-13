from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    places_list = request.session.get('places_list', [])
    return render(request, 'wheretogo/home.html', {'places': places_list})


def places(request):
    places_list = request.session.get('places_list', [])
    return render(request, 'wheretogo/places.html', {'places': places_list})


def add_place(request):
    if request.method == 'POST':
        places_list = request.session.get('places_list', [])
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
