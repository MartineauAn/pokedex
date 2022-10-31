from django.shortcuts import render, HttpResponse



def index(request):
    text = "<h1> Hello world ! </h1>"
    return render(request,"pokedexapp/dashboard.html",{})
