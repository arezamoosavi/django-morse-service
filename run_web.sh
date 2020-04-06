#!/bin/bash
#python manage.py test

sleep 10

cd src

python manage.py makemigrations
python manage.py migrate

python manage.py test

python manage.py runserver 0.0.0.0:8000
exec "$@"