# Work In Progress

This application will use a Django backend to write the number of heads or tails in a PostgreSQL database.

Once 5 heads have been made, a big secret will be revealed to the user.

The application will be containerised and a chart helm will be produced.

The educational aim will be to secure access to the database via a dynamic secret and also to secure the secret revealed by the application in Vault.

# Travail en cours

Cette application utilisera un backend Django pour écrire le nombre de pile ou de face en base de données PostgreSQL.

Une fois 5 faces réalisé, un lourd secret sera révélé à l'utilisateur.

L'application sera conteneurisée et un chart helm sera réalisé.

Le but pédagogique sera de sécuriser les accès à la base de donnée via un secret dynamique et également de mettre en sécurité dans Vault, le secret que révèlera l'application.

# Initial setup

```shell
python -m venv .pyenv
source .pyenv/bin/activate

pip install django
pip install 'environs[django]'
pip freeze > requirements.txt
```

```shell
mkdir src && cd src

django-admin startproject coin-to-flip .

python manage.py migrate
python manage.py runserver
```

# Setup

```shell
python -m venv .pyenv
source .pyenv/bin/activate

pip install -r requirements.txt

python manage.py runserver
```
