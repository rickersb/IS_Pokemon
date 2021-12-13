from django.db import connection
from django.shortcuts import render
from homepages.models import PokemonInfo, PokemonType
# Create your views here.

def indexPageView(request):
    if request.method == "GET" and "pokemon" in request.GET:
        pokemons = PokemonInfo.objects.filter(name__icontains=request.GET['pokemon'])
    else:
        pokemons = PokemonInfo.objects.all()
    data = {
        'pokemons': pokemons
    }
    return render(request, 'homepages/index.html', data)

def detailsPageView(request, pokemon):
    pokemon_obj = PokemonInfo.objects.get(pokemon_id=pokemon)
    #type = PokemonType.objects.filter(pokemon__in=pokemon)
    cursor = connection.cursor()
    query = "SELECT type FROM pokemon_type WHERE pokemon_id=%s"
    cursor.execute(query, [pokemon])
    columns = [col[0] for col in cursor.description]
    type = [dict(zip(columns, row)) for row in cursor.fetchall()]
    data = {
        'pokemon': pokemon_obj,
        'type': type,
    }
    return render(request, 'homepages/details.html', data)

def showPokemonPageView(request):
    data = PokemonInfo.objects.all()
    context = {
        "poke" : data
    }
    return render(request, 'homepages/showPokemon.html', context)

def showSinglePokemonPageView(request, pokemon_id):
    data = PokemonInfo.objects.get(pokemon_id = pokemon_id)
    cursor = connection.cursor()
    query = "SELECT type FROM pokemon_type WHERE pokemon_id=%s"
    cursor.execute(query, [pokemon_id])
    columns = [col[0] for col in cursor.description]
    type = [dict(zip(columns, row)) for row in cursor.fetchall()]
    if len(type) < 2:
        type1 = type[0]['type']
        type2 = 'None'
    else :
        type1 = type[0]['type']
        type2 = type[1]['type']
    context = {
        "record": data,
        "type1": type1,
        "type2": type2,
    }

    return render(request, 'homepages/editPokemon.html', context)

def updatePokemonPageView(request):
    if request.method == "POST":
        pokemon_id = request.POST['pokemon_id']

        pokemon = PokemonInfo.objects.get(pokemon_id=pokemon_id)
        type1 = request.POST['type1']
        type2 = request.POST['type2']
        print(type2)
        cursor = connection.cursor()
        query = "SELECT type FROM pokemon_type WHERE pokemon_id=%s"
        cursor.execute(query, [pokemon_id])
        columns = [col[0] for col in cursor.description]
        type = [dict(zip(columns, row)) for row in cursor.fetchall()]
        if type2 == 'None':
            if len(type) < 2:
                cursor = connection.cursor()
                query = "UPDATE pokemon_type SET type=%s WHERE pokemon_id=%s"
                cursor.execute(query, (type1, pokemon_id))
            else:
                cursor = connection.cursor()
                query = "DELETE FROM pokemon_type WHERE pokemon_id=%s and type=%s"
                cursor.execute(query, (pokemon_id, type[1]['type']))
                cursor = connection.cursor()
                query = "UPDATE pokemon_type SET type=%s WHERE pokemon_id=%s and type=%s"
                cursor.execute(query, (type1, pokemon_id, type[0]['type']))
        else:
            if len(type) < 2:
                cursor = connection.cursor()
                query = "UPDATE pokemon_type SET type=%s WHERE pokemon_id=%s"
                cursor.execute(query, (type1, pokemon_id))
                cursor = connection.cursor()
                query = "INSERT INTO pokemon_type(pokemon_id, type) VALUES(%s, %s)"
                cursor.execute(query, (pokemon_id, type2))
            else:
                cursor = connection.cursor()
                query = "UPDATE pokemon_type SET type=%s WHERE pokemon_id=%s and type=%s"
                cursor.execute(query, (type1, pokemon_id, type[0]['type']))
                cursor = connection.cursor()
                query = "UPDATE pokemon_type SET type=%s WHERE pokemon_id=%s and type=%s"
                cursor.execute(query, (type2, pokemon_id, type[1]['type']))
                print('2 types')

        pokemon.name = request.POST['name']
        pokemon.image_path = request.POST['image_path']
        pokemon.height = request.POST['height']
        pokemon.weight = request.POST['weight']
        pokemon.description = request.POST['description']
        pokemon.region = request.POST['region']

        pokemon.save()
    return showPokemonPageView(request)

def deletePokemonPageView(request, pokemon_id):
    data = PokemonInfo.objects.get(pokemon_id = pokemon_id)
    data.delete()
    return showPokemonPageView(request)

def addPokemonPageView(request):
    if request.method == "POST":

        pokemon = PokemonInfo()
        cursor = connection.cursor()
        query = "SELECT max(pokemon_id) as max from pokemon_info"
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        temp = [dict(zip(columns, row)) for row in cursor.fetchall()]
        pokemon_id = temp[0]['max'] +1
        
        pokemon.pokemon_id = pokemon_id
        pokemon.name = request.POST['name']
        pokemon.image_path = 'img/' + request.POST['image_path']
        pokemon.height = request.POST['height']
        pokemon.weight = request.POST['weight']
        pokemon.description = request.POST['description']
        pokemon.region = request.POST['region']
        

        pokemon.save()
        return showPokemonPageView(request)
    else:
        return render(request, 'homepages/addPokemon.html')




