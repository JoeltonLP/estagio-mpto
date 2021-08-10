
from helprs.serializer import BaseSerializer
from .models import (
    State,
    City, 
    Person, 
    NaturalPerson, 
    LegalPerson,
    PackageContainer,
    LogTrace
)

class PackageContainerSerilizer(BaseSerializer):
    _model = PackageContainer

    @classmethod
    def encode(cls, instance):

        result = super().encode(instance)

        result.update(
            sender=PersonSerializer.encode(instance.sender),
            destination=PersonSerializer.encode(instance.destination),
            sender_city=CitySerializer.encode(instance.sender_city),
            destination_city=CitySerializer.encode(instance.destination_city),
            weight=float(instance.weight),
            volume=float(instance.volume),
            create_at=str(instance.create_at),
            unique_identify=instance.unique_identify,
            delivery_state=instance.delivery_state,
            delivery_state_display=instance.get_delivery_state_display()
        )

        return result


class PersonSerializer(BaseSerializer):
    _model = Person

    @classmethod
    def encode(cls, instance):
       
        result = super().encode(instance)

        result.update(
            name=instance.name,
            city=CitySerializer.encode(instance.city)
        )

        return result

class NaturalPersonSerializer(PersonSerializer):
    _model = NaturalPerson

    @classmethod
    def encode(cls, instance):
        result = super().encode(instance)

        result.update(
           cpf = instance.cpf
        )

        return result

class LegalPersonSerializer(PersonSerializer):
    _model = LegalPerson

    @classmethod
    def encode(cls, instance):
       
        result = super().encode(instance)

        result.update(
            fantasy_name=instance.fantasy_name,
            cnpj=instance.cnpj
        )

        return result

class StateSerializer(BaseSerializer):
    # tracker.models.State
    _model = State

    @classmethod
    def encode(cls, instance):
        result = super().encode(instance)

        result.update(
            name=instance.name,
            abbreviation=instance.abbreviation
        )

        return result

class CitySerializer(BaseSerializer):
    _model = City
   
    @classmethod
    def encode(cls, instance):
        result = super().encode(instance)

        result.update(
            name=instance.name,
            state=StateSerializer.encode(instance.state)
            #state_name=instance.state.name,
            #state_abbreviation=instance.state.abbreviation
        )

        return result


class LogTraceSerializer(BaseSerializer):
    _model = LogTrace