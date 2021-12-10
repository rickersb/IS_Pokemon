from django.shortcuts import render
from homepages.models import Pokemon, PokemonType
# Create your views here.

def indexPageView(request):
    return render(request, 'homepages/index.html')


def showPokemonPageView(request):
    data = Pokemon.objects.all()
    context = {
        "poke" : data
    }
    return render(request, 'homepages/showPokemon.html', context)

def showSinglePokemonPageView(request, pokemon_id):
    data = Pokemon.objects.get(pokemon_id = pokemon_id)

    context = {
        "record": data
    }

    return render(request, 'homepages/editPokemon.html', context)

def updatePokemonPageView(request):
    if request.method == "POST":
        pokemon_id = request.POST['pokemon_id']

        pokemon = Pokemon.objects.get(pokemon_id=pokemon_id)

        pokemon.name = request.POST['name']
        pokemon.image_path = request.POST['image_path']
        pokemon.height = request.POST['height']
        pokemon.weight = request.POST['weight']
        pokemon.description = request.POST['description']
        pokemon.region = request.POST['region']

        pokemon.save()
    return showPokemonPageView(request)

def deletePokemonPageView(request, pokemon_id):
    data = Pokemon.objects.get(pokemon_id = pokemon_id)
    data.delete()
    return showPokemonPageView(request)

def addPokemonPageView(request):
    if request.method == "POST":

        pokemon = Pokemon()

        pokemon.pokemon_id = request.POST['pokemon_id']
        pokemon.name = request.POST['name']
        pokemon.image_path = request.POST['image_path']
        pokemon.height = request.POST['height']
        pokemon.weight = request.POST['weight']
        pokemon.description = request.POST['description']
        pokemon.region = request.POST['region']
        

        pokemon.save()
        return showPokemonPageView(request)
    else:
        return render(request, 'homepages/addPokemon.html')




