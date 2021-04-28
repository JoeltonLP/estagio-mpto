from django.db import models


class State(models.Model):
    name = models.CharField('nome', max_length=100)
    abbreviation = models.CharField('sigla', max_length=2, unique=True)

    def __str__(self):
        return f'{self.name}/{self.abbreviation}'


class City(models.Model):
    name = models.CharField('nome', max_length=100, unique=True)
    state = models.ForeignKey(
        State, related_name='cities', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}/{self.state.abbreviation}'
