from .models import State, City, Person, NaturalPerson, LegalPerson
from helprs.serializer import BaseSerializer

class PersonSerializer(BaseSerializer):
    _model = Person

class NaturalPersonSerializer(PersonSerializer):
    _model = NaturalPerson

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



