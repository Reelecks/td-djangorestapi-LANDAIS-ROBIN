# Research Projet Tracker / TD DJANGO ROBIN LANDAIS

Ce projet est une application Django pour le suivi de projets de recherche, permettant de gérer les chercheurs, les projets de recherche et les publications associées. Il comprend une interface utilisateur complète ainsi que des routes API sécurisées par JWT.

#### Prérequis
- Python 3.x
- pip
- Git

### Coner le projet : 
#### Étapes : 
Clonez le dépôt :
git clone https://github.com/YOUR_GITHUB_USERNAME/td-djangorestapi-LANDAIS-ROBIN.git
cd td-djangorestapi-LANDAIS-ROBIN


Créez et activez un environnement virtuel :
python -m venv env
source env/bin/activate  # Pour Unix/macOS
env\Scripts\activate  # Pour Windows


Installez les dépendances :
pip install -r requirements.txt


Appliquez les migrations de la base de données :
python manage.py makemigrations
python manage.py migrate


Créez un superutilisateur :
python manage.py createsuperuser  


Lancez le serveur de développement :
python manage.py runserver


Accédez à l'application :
Ouvrez votre navigateur et accédez à http://localhost:8000.