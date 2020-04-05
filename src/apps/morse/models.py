from django.db import models

class ReceiveSentence(models.Model):
    sentence = models.CharField(max_length = 100)
    receive_date = models.DateField(auto_now_add = True)

class MorseCombination(models.Model):
    word = models.CharField(max_length = 1)
    combination = models.CharField(max_length = 8)
