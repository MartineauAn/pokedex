
# Préparation
- Installation de virtualenv :
	-  Créer un dossier "python"
	- Se placer dedans via un cmd ou le terminal de vscode
	- Executer la commande "pip  install  virtualenv" pour installer les environnements virutels
	- Créer l'environnement virtuel pour le pokédex avec : "python -m venv django-pokedex"
	- Toujours dans le dossier python utiliser la commande : "django-pokedex\Scripts\activate"
	- Si erreur à la commande précédente, utiliser : "Set-ExecutionPolicy Unrestricted -Force"
	- Sinon il devrait y avoir "(django-pokedex)" dans le terminal

# Récupération du projet
	git clone https://github.com/MartineauAn/pokedex.git
- Renommer db.sqlite3.example en db.sqlite3
- Installation des packages :
	- Installer les packages dans le installation.txt
- Lancer les migrations : "python manage.py migrate"
- Créer un admin pour la base de données : "python manage.py createsuperuser" => remplir les infos

# Remarques pour django
- Pour lancer le serveur web : "Python manage.py runserver"
- Pour accéder au panel admin : http://127.0.0.1:8000/admin

# Présentation

## Technologies utilisées 

Ce projet a été réalisé à l'aide de [Django](https://www.djangoproject.com/), un framework opensource web en Python, pour la partie backend.

Afin de rendre l'experience utilisateur plus agréable et d'éviter des chargements de pages fréquents, nous avons utilisé des requêtes [AJAX](https://developer.mozilla.org/fr/docs/Web/Guide/AJAX) pour l'affichage des pokémon.

Pour la partie frontend, nous avons opté pour [Tailwind css](https://tailwindcss.com/).

Pour finir, nous avons testé la librairie Javascript [Three js](https://threejs.org/) avec les modules [OrbitControls](https://threejs.org/docs/#examples/en/controls/OrbitControls) et [GLTFLoader](https://threejs.org/docs/?q=gltf#examples/en/loaders/GLTFLoader) pour pouvoir visualiser l'ensemble des pokémons en 3D.

## Fonctionnalités

Le projet comporte 3 vues :

- Une page d'accueil pour aiguiller l'utilisateur
- Une vue "Pokédex" avec :
	- Le choix des pokémons parmis une liste déroulante
	- Une fonction de recherche de Pokémon par numéro ou nom
	- L'affichage de chaque pokémon en 3D avec possibilité de le faire bouger 
	- L'affichage des informations de chaque pokémon
	- La possibilité de pouvoir écouter le cri de chaque Pokémon
	- La possibilité de l'affichage des pokémon entre 2D et 3D
- Une vue "Equipes" pour la gestion des équipes Pokémon :
	- La possiblité d'ajouter des équipes de 6 Pokémon 
	- La possibilité d'ajouter / modifier les Pokémon d'une équipe
	- La possiblité de changer le nom d'une équipe
	- La possibilité de supprimer une équipe
	- Une fonction de recherche équivalente à celle du pokédex

## Utilisation de l'api

L'api des [Pokémon](https://pokeapi.co/) a été utilisée pour :
- Récupérer l'ensemble des 151 premiers Pokémon
- Récupérer les informations d'un Pokémon
- Récupérer l'ensemble des types de Pokémon 

# Auteurs du projet
Ce projet a été réalisé par
- Antoine Martineau
- Cyprien Rimbaud
- Nathanaël Ka
- Alexis Def
