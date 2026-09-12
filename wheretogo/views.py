from django.shortcuts import render, redirect


def home(request):
    return render(request, 'wheretogo/home.html')


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
            'rating': int(rating) if rating else None
        }
        places_list.append(new_place)
        request.session['places_list'] = places_list
        request.session.modified = True
        return redirect('places')
    return render(request, 'wheretogo/add_place.html')
