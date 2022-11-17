from .models import Teams
from django.forms import ModelForm  

class TeamsForm(ModelForm):
    class Meta:
        model = Teams
        fields = '__all__'