from .models import Teams
from django import forms  

class TeamsForm(forms.Form):
    pokemon_1_id = forms.IntegerField()
    pokemon_2_id = forms.IntegerField()
    pokemon_3_id = forms.IntegerField()
    pokemon_4_id = forms.IntegerField()
    pokemon_5_id = forms.IntegerField()
    pokemon_6_id = forms.IntegerField()