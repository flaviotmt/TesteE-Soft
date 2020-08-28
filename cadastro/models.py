from django.db import models

# Create your models here.

class Pessoas(models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length = 30)
    idade = models.IntegerField()
    nascimento = models.DateField()
    email = models.EmailField(max_length = 70)
    apelido = models.CharField(max_length = 20, null = True)
    obs = models.CharField(max_length = 100, null = True)