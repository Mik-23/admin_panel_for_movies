from django.shortcuts import render
from .models import *

# Create your views here.
genre = Genre.objects.all()
film = Filmwork.objects.order_by('modified')
person = Person.objects.all()
print(genre)
print(film)
print(person)

def panel_home(request):
    return render(request, 'panel/panel_home.html', {'genre': genre})

def film_home(request):
    return render(request, 'panel/film_home.html', {'film': film})

def person_home(request):
    return render(request, 'panel/person_home.html', {'person': person})