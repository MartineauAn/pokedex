from django.urls import path

from . import views

urlpatterns = [
    path('', views.pokedex, name="index"),
    path('teams',views.teams, name="pokedex"),

]
