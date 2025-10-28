from django.urls import path
from . import views

urlpatterns = [
    path('pokedex/', views.index, name='index'),
    path('pokedex/<str:pokemon>/', views.pokemons_details, name='pokemon_details'),
]
