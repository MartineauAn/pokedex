# Generated by Django 4.1.3 on 2022-11-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipe_id', models.IntegerField()),
                ('pokemon_id', models.IntegerField()),
            ],
        ),
    ]
