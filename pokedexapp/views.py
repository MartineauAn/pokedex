from django.shortcuts import render, HttpResponse
import requests
from .forms import TeamsForm


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
    form = TeamsForm()

    if request.method == 'POST':
        print(request.POST)
        
    context = {'form' : form}
    return render(request,"pokedexapp/teams.html",context)