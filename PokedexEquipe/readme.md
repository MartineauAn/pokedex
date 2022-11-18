# Préparation
- Installation de virtualenv :
	-  Créer un dossier "python"
	- Se placer dedans via un cmd ou le terminal de vscode
	- Executer la commande "pip  install  virtualenv" pour installer les environnements virutels
	- Créer l'environnement virtuel pour le pokédex avec : "python -m venv django-pokedex"
	- toujours dans le dossier python utiliser la commande : "django-pokedex\Scripts\activate"
	- Si erreur à la commande précédentte, utiliser : "Set-ExecutionPolicy Unrestricted -Force"
	- Sinon il devrait y avoir "(django-pokedex)" dans le terminal

# Récupération du projet
	git init
	git remote add origin https://github.com/MartineauAn/pokedex
	git pull origin master
	git branch "ma branche"
	git checkout "ma branche"
- Renommer db.sqlite3.example en db.sqlite3
- Installation des packages :
	- Installer à coups de "pip install" les packages dans le installation.txt
- Lancer les migrations : "python manage.py migrate"
- Créer un admin pour la base de données : "python manage.py createsuperuser" => remplir les infos

# Remarques pour django
- Pour lancer le serveur web : "Python manage.py runserver"
- Pour accéder au panel admin : http://127.0.0.1:8000/admin

# Au moindre problème --> me contacter :baby_chick: