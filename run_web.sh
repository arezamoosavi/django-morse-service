#!/bin/bash
#python manage.py test
python manage.py makemigrations
python manage.py migrate

pthon manage.py test

python manage.py runserver 0.0.0.0:8000
exec "$@"