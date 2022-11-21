
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

Ce projet à été réalisé à l'aide du framework python [Django](https://www.djangoproject.com/) pour la partie backend.

Afin de rendre l'experience utilisateur plus agréable et d'éviter des chargements de pages fréquents, nous avons utilisé des requêtes [AJAX](https://developer.mozilla.org/fr/docs/Web/Guide/AJAX) pour l'affichage des pokémon.

Pour la partie frontend, nous avons opté pour [Tailwind css](https://tailwindcss.com/).

Pour finir, nous avons testé la librairie Javascript [Three js](https://threejs.org/) avec les modules [OrbitControls](https://threejs.org/docs/#examples/en/controls/OrbitControls) et [GLTFLoader](https://threejs.org/docs/?q=gltf#examples/en/loaders/GLTFLoader) pour pouvoir visualiser l'ensemble des pokémons en 3D.

## Fonctionnalités

Le projet comporte 3 vues :

- Une page d'accueil pour aiguiller l'utilisateur
- Une vue pour le pokedex avec :
	- Le choix des pokémons parmis une liste déroulante
	- Une fonction de recherche de pokémon par numéro ou nom
	- L'affichage de chaque pokémon en 3D avec possibilité de le faire bouger 
	- L'affichage des informations de chaque pokémons
	- La possibilité de pouvoir écouter le cri de chaque pokémon
	- La possibilité de l'affichage des pokémon entre 2D et 3D
- Une vue pour la gestion des équipes avec :
	- La possiblité d'ajouter des équipes de 6 pokémon 
	- La possibilité d'ajouter / modifier les pokémon d'une équipes
	- La possiblité de changer le nom d'une équipe
	- La possibilité de supprimer une équipe
	- Une fonction de recherche équivalente à celle du pokédex

## Utilisation de l'api

L'api des [pokémons](https://pokeapi.co/) a été utilisée pour :
- Récupérer l'ensembles des 151 premier pokémons
- Récupérer les informations d'un pokémon
- Récupérer l'ensemble des types de pokémons 
