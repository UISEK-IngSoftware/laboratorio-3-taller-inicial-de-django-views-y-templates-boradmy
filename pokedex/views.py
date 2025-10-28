from django.shortcuts import render

# Create your views here.
def index(request):
    pokemons = ['pikachu', 'charmander', 'bulbasaur', 'squirtle', 'jigglypuff', 'meowth', 'psyduck', 'snorlax', 'eevee', 'mewtwo']
    return render(request, 'index.html', {
        'pokemons': pokemons
        })
def pokemons_details(request, pokemon):
    return render(request, 'pokemon_details.html', {
        'pokemon': pokemon
    })