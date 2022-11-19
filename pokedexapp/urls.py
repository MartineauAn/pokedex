from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pokedex',views.pokedex, name="pokedex"),
    path('teams',views.teams, name="teams"),
    path('teams/all',views.teamsAll, name="teamAll"),
    path('teams/update',views.teamUpdate, name="teamUpdate"),
    path('teams/delete/<int:team>', views.teamDelete, name="teamDelete"),
    path('teams/add', views.teamAdd, name="teamAdd"),
    path('teams/update/name/<int:id>',views.teamNameUpdate, name="teamNameUpdate")

]
