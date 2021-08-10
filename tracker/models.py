import os
import base64
import hashlib

from django.db import models
from django.db.models.fields import CharField


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


class Person(models.Model):
    name = models.CharField('Nome', max_length=200)
    city = models.ForeignKey(City, related_name='+', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name


class NaturalPerson(Person):
    cpf = models.CharField('cpf', max_length=11, unique=True)

    def __str__(self):
        return f'{self.name} ({self.cpf})'


class LegalPerson(Person):
    fantasy_name = models.CharField('fantasy_name', max_length=200)
    cnpj = models.CharField('cnpj', max_length=11, unique=True)

    def __str__(self):
        return f'{self.fantasy_name} ({self.cnpj})'


class PackageContainer(models.Model):
    sender = models.ForeignKey(
        Person, 
        related_name='as_sender_of', 
        on_delete=models.PROTECT
    )
    destination = models.ForeignKey(
        Person, 
        related_name='as_destination_of', 
        on_delete=models.PROTECT
    )
    sender_city = models.ForeignKey(City, related_name='as_origin_of', on_delete=models.PROTECT)
    destination_city = models.ForeignKey(
        City, 
        related_name='as_destination_of', 
        on_delete=models.PROTECT
    )
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    volume = models.DecimalField(max_digits=5, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    unique_identify = models.CharField(max_length=5, unique=True, db_index=True)
    delivery_state = models.SmallIntegerField(
        choices=(
            (1, 'Na origem'),
            (2, 'Em trânsito'),
            (3, 'No destino'),
            (4, 'Entregue'),
            (5, 'Extraviado')
        ),
        default=1
    )

    

    def __str__(self):
        return f'Pacote #{self.unique_identify} - {self.get_delivery_state_display()}'

    #Preciso que ao cadastrar um novo package que este tenho um numero não sequencial e unico #35

    def _generate_unique_identify(self):

        print('XX', self)

        return hashlib.new(
            'md5',
            base64.b64encode(
                os.urandom(4096)
            )
        ).hexdigest()[:8]

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sender_city = self.sender.city
            self.destination_city = self.destination.city
            self.unique_identify = self._generate_unique_identify()

        super().save(*args, **kwargs)

class LogTrace(models.Model):
    package_container = models.ForeignKey(
        PackageContainer, 
        related_name='logs', 
        on_delete=PackageContainer
    )

    city = models.ForeignKey(
        City, 
        related_name='+',
        on_delete=City
    )

    when = models.DateTimeField(auto_now_add=True)

