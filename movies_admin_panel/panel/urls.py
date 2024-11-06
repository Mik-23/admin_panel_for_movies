from django.urls import path
from . import views

urlpatterns = [
    path('genre/', views.panel_home, name='genre'),
    path('film/', views.film_home, name='film'),
    path('person/', views.person_home, name='person')
]