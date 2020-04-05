from django.urls import path

from apps.morse import views

app_name = 'morse_service'

urlpatterns = [
    path('morse',
            views.TranslatetoMorse.as_view(),
            name='translate'),
    path('queue',
            views.QueueMesseges.as_view(),
            name='queue'),
]