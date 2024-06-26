# Research Projet Tracker / TD DJANGO ROBIN LANDAIS

Ce projet est une application Django pour le suivi de projets de recherche, permettant de gérer les chercheurs, les projets de recherche et les publications associées. Il comprend une interface utilisateur complète ainsi que des routes API sécurisées par JWT.

#### Prérequis
- Python 3.x
- pip
- Git

### Coner le projet : 
#### Étapes : 
Clonez le dépôt :
```bat
git clone https://github.com/YOUR_GITHUB_USERNAME/td-djangorestapi-LANDAIS-ROBIN.git
cd td-djangorestapi-LANDAIS-ROBIN
``` 

Créez et activez un environnement virtuel :
```bat
python -m venv env
source env/bin/activate  # Pour Unix/macOS
env\Scripts\activate  # Pour Windows
``` 

Installez les dépendances :
```bat
pip install -r requirements.txt
``` 

Appliquez les migrations de la base de données :
```bat
python manage.py makemigrations
python manage.py migrate
``` 

Créez un superutilisateur :
```bat
python manage.py createsuperuser  
``` 

Lancez le serveur de développement :
```bat
python manage.py runserver
``` 

Accédez à l'application :
Ouvrez votre navigateur et accédez à http://localhost:8000.

### Utilisation : 


#### Interface Utilisateur :
- Login : http://localhost:8000/login/
- Inscription : http://localhost:8000/register/
- Liste des chercheurs : http://localhost:8000/chercheurs/
- Liste des projets de recherche : http://localhost:8000/projets/
- Liste des publications : http://localhost:8000/publications/
- Recherche avancée : http://localhost:8000/search/

#### Routes API : 

##### Authentification 
Pour récuperer un jeton il faut d'abord s'inscrire sur le frontend : http://localhost:8000/register/
Pour plus d'informations utiliser : http://localhost:8000/redoc ou http://localhost:8000/swagger
URL : http://localhost:8000/api/token/
Méthode : POST

Corps de la requête : x-www-form-urlencoded

username: your_username
password: your_password

Exemple de réponse :

{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}


Utiliser le jeton d'accès :
Ajoutez le header Authorization avec la valeur Bearer your_access_token à vos requêtes.

Endpoints CRUD :

Chercheurs :
Lister et créer :
URL : http://localhost:8000/api/chercheurs/
Méthode : GET (Lister), POST (Créer)
Détails, mise à jour et suppression :
URL : http://localhost:8000/api/chercheurs/<id>/
Méthode : GET (Détails), PUT (Mise à jour), DELETE (Suppression)


Projets de recherche :

Lister et créer :
URL : http://localhost:8000/api/projets/
Méthode : GET (Lister), POST (Créer)
Détails, mise à jour et suppression :
URL : http://localhost:8000/api/projets/<id>/
Méthode : GET (Détails), PUT (Mise à jour), DELETE (Suppression)


Publications :

Lister et créer :
URL : http://localhost:8000/api/publications/
Méthode : GET (Lister), POST (Créer)
Détails, mise à jour et suppression :
URL : http://localhost:8000/api/publications/<id>/
Méthode : GET (Détails), PUT (Mise à jour), DELETE (Suppression)


### Explication du fichier test.http
- Obtention et rafraîchissement des jetons d'accès : Les premières requêtes permettent d'obtenir et de rafraîchir le jeton d'accès nécessaire pour accéder aux routes protégées de l'API.
- equêtes CRUD pour les chercheurs, projets de recherche et publications : Chaque entité a des requêtes pour lister, créer, obtenir les détails, mettre à jour et supprimer les entrées.
### Instructions pour l'utilisation
- Inscrivez vous dabord sur la palteforme web pour créer un compte
- Remplissez les valeurs your_username et your_password avec les informations de connexion de votre utilisateur.
- Obtenez le access_token en exécutant la première requête.
- Utilisez le access_token obtenu dans les requêtes suivantes en remplaçant {{access_token}}.
- Utilisez un outil comme VS Code avec l'extension REST Client ou Postman pour exécuter ces requêtes.