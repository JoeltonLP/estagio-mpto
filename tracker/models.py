from django.db import models


class State(models.Model):
    name = models.CharField('nome', max_length=100)
    abbreviation = models.CharField('sigla', max_length=2, unique=True)
