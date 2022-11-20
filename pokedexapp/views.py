from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
from .forms import TeamsForm
from .models import Teams


def index(request):
    return render(request,"pokedexapp/dashboard.html",{})


def pokedex(request):
    req = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=151")
    if req.status_code == 200 :
        pokemon = req.json()
    else :
        pokemon = {}

    req = requests.get("https://pokeapi.co/api/v2/type")
    if req.status_code == 200 :
        types = req.json()
        for type in types["results"]:
            if type["name"] == "normal":
                type["color"] = "bg-stone-400"
            elif type["name"] == "fire":
                type["color"] = "bg-orange-500"
            elif type["name"] == "water":
                type["color"] = "bg-blue-500"
            elif type["name"] == "grass":
                type["color"] = "bg-green-400" 
            elif type["name"] == "electric":
                type["color"] = "bg-yellow-300"
            elif type["name"] == "ice":
                type["color"] = "bg-cyan-400"
            elif type["name"] == "fighting":
                type["color"] = "bg-amber-700"     
            elif type["name"] == "poison":
                type["color"] = "bg-violet-600"
            elif type["name"] == "ground":
                type["color"] = "bg-yellow-600"  
            elif type["name"] == "flying":
                type["color"] = "bg-purple-400"
            elif type["name"] == "psychic":
                type["color"] = "bg-pink-500"
            elif type["name"] == "bug":
                type["color"] = "bg-lime-600"
            elif type["name"] == "rock":
                type["color"] = "bg-yellow-700"
            elif type["name"] == "ghost":
                type["color"] = "bg-violet-900"
            elif type["name"] == "dark":
                type["color"] = "bg-yellow-900"
            elif type["name"] == "dargon":
                type["color"] = "bg-purple-800"
            elif type["name"] == "steel":
                type["color"] = "bg-gray-400" 
            elif type["name"] == "fairy":
                type["color"] = "bg-rose-400"                                                               
    else :
        types = {}

    return render(request,"pokedexapp/pokedex.html",{"pokemon":pokemon,"types":types})

def teams(request):
    req = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=151")
    if req.status_code == 200 :
        pokemon = req.json()
    else :
        pokemon = {}

    return render(request,"pokedexapp/teams.html",{"pokemon":pokemon})

def teamsAll(request):
    teams = Teams.objects.all()
    return render(request,"pokedexapp/ajax/teams.html",{"teams":teams})

def teamAdd(request):
    if request.method == 'POST':
        if request.POST.get("name") != "":
            name = request.POST.get("name")
            try:
                team = Teams.objects.get(name=name)
                return JsonResponse({"message": "Équipe déjà existante"}, status=500)
            except:
                team = Teams(name=name)
                team.save()
                return JsonResponse({"message": "Équipe créée avec succès"})

    return JsonResponse({"message": "Une erreur est survenue"}, status=500)
    
    

def teamUpdate(request):

    if request.method == 'POST':
        teamR = request.POST.get("team")
        positionR = request.POST.get("position")
        pokemonR = request.POST.get("pokemon")

        try:
            teamR = int(teamR)
            positionR = int(positionR)
            pokemonR = int(pokemonR)  
        except:
            JsonResponse({"message": "Erreur dans les paramètres"}, status=500)

            print(teamR,positionR, pokemonR)
        
        if teamR != 0 and positionR > 0 and pokemonR > 0 and positionR <= 6 and pokemonR <= 151:
            try:
                field = "pokemon_" + str(positionR) + "_id"
                team = Teams.objects.get(id=teamR)
                setattr(team, field, pokemonR)
                team.save()
                return JsonResponse({"message": "Pokémon ajouté dans l'équipe"})
            except:
                return JsonResponse({"message": "Équipe inexistante"}, status=500)
        else:
            return JsonResponse({"message": "Erreur dans les paramètres"}, status=500)

    return JsonResponse({"message": "Une erreur est survenue"}, status=500)

def teamNameUpdate(request,id):
    if request.method == 'POST':
        if request.POST.get("name") != "":
            name = request.POST.get("name")
            try:
                team = Teams.objects.get(name=name)
                if team.id == id:
                    return JsonResponse({"message": "Veuillez entrer un nom différent"}, status=500)
                else:
                    return JsonResponse({"message": "Équipe déjà existante"}, status=500)
            except:
                team = Teams.objects.get(id=id)
                team.name = name
                team.save()
                return JsonResponse({"message": "Nom de l'équipe modifié avec succès"})

    return JsonResponse({"message": "Une erreur est survenue"}, status=500)


def teamDelete(request, team):
    if request.method == 'DELETE':
        try:
            Teams.objects.get(id=team).delete()
            return JsonResponse({"message": "Équipe supprimée avec succès"})
        except:
            return JsonResponse({"message": "Erreur dans les paramètres"}, status=500)

    return JsonResponse({"message": "Une erreur est survenue"}, status= 500)