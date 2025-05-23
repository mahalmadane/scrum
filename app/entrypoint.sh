#!/bin/bash
echo "Attente que la base de données soit prête..."
while ! nc -z db 5432; do
  sleep 1
done
echo "La base de données connecteé. Démarrage de l'application... !"

python manage.py migrate

gunicorn config.wsgi:application --bind 0.0.0:8000 