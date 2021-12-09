from django.shortcuts import render
from homepages.models import Pokemon, Trainerinfo
# Create your views here.

def indexPageView(request):
    return render(request, 'homepages/index.html')


def showPokemonPageView(request):
    data = Pokemon.objects.all()
    context = {
        "poke" : data
    }
    return render(request, 'homepages/showPokemon.html', context)

def showSinglePokemonPageView(request, poke_id):
    data = Pokemon.objects.get(id = poke_id)

    context = {
        "record": data,
    }

    return render(request, 'homepages/editPokemon.html', context)

def updatePokemonPageView(request):
    if request.method == "POST":
        poke_id = request.POST['poke_id']

        pokemon = Pokemon.objects.get(id=poke_id)

        pokemon.first_name = request.POST['poke_name']
        pokemon.last_name = request.POST['poke_type']

        pokemon.save()
    return showPokemonPageView(request)

def deletePokemonPageView(request, poke_id):
    data = Pokemon.objects.get(id = poke_id)
    data.delete()
    return showPokemonPageView(request)

def addPokemonPageView(request):
    if request.method == "POST":

        pokemon = Pokemon()

        pokemon.first_name = request.POST['poke_name']
        pokemon.last_name = request.POST['poke_type']
        

        pokemon.save()
        return showPokemonPageView(request)
    else:
        return render(request, 'homepages/addPokemon.html')




