# Generated by Django 4.1.2 on 2022-11-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedexapp', '0004_remove_teams_equipe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]