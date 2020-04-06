# About

This project is a web service that translate text to Morse code and send it to log server. Build with django rest framework and uses celery and rabbitmq for asynchronous tasks.

## Installation


```bash
docker-compose up --build
```

## Run Tests

first get into app container shell by:
```bash
docker-compose exec app sh
```
then run tests by

```bash
python manage.py test
```