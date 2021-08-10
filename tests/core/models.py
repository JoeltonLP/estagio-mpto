from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, related_name='vacas', on_delete=models.PROTECT)
