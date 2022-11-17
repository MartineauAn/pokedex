from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pokedex',views.pokedex, name="pokedex"),
    path('teams',views.teams, name="teams"),

]
