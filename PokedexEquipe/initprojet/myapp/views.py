import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = { 'Titi': "blablabla rominet"}
    return render(request, 'index.html', context)

def hello(request):
    return HttpResponse("test")