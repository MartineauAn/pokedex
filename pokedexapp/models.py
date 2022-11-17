from django.db import models

# Create your models here.

class Teams(models.Model):
    pokemon_1_id = models.IntegerField(default=None, blank=True, null=True)
    pokemon_2_id = models.IntegerField(default=None, blank=True, null=True)
    pokemon_3_id = models.IntegerField(default=None, blank=True, null=True)
    pokemon_4_id = models.IntegerField(default=None, blank=True, null=True)
    pokemon_5_id = models.IntegerField(default=None, blank=True, null=True)
    pokemon_6_id = models.IntegerField(default=None, blank=True, null=True)

    def saveTeam(self):
        self.save()
