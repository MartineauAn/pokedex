from django.shortcuts import render, HttpResponse
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
    return render(request,"pokedexapp/pokedex.html",{"pokemon":pokemon})

def teams(request):

    req = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=151")
    if req.status_code == 200 :
        pokemon = req.json()
    else :
        pokemon = {}


    form = TeamsForm()
    try:
        print(Teams.objects.get(id=1).pokemon_1_id)
    except:
        print('Introuvable zebi')

    team = Teams.objects.get(id=1)
    team.pokemon_1_id = 2
    team.save()

    if request.method == 'POST':
        print(request.POST)
        # form.save()
    context = {'form' : form, 'pokemon': pokemon}
    return render(request,"pokedexapp/teams.html",context)


# def saveTeams(request):

#     if request.method == 'POST':
#         print(request)
#         new team = Teams()
#         team.save()

    