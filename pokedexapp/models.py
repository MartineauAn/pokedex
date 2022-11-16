from django.db import models

# Create your models here.

class Teams(models.Model):
    equipe_id = models.IntegerField()
    pokemon_id = models.IntegerField()

    def saveTeam(self):
        self.save()

    def getTeam(self):
        pass