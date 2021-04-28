from .models import State, City


class BaseSerialization:

    _model = None

    @classmethod
    def Model(cls):
        return cls._model

    @classmethod
    def serializer(cls, instance):
        return {
            'pk': instance.pk,
            'description': str(instance)
        }

    @classmethod
    def deserializer(cls, data):
        return cls._model(**data)

        


class StateSerializer(BaseSerialization):
    # tracker.models.State
    _model = State

    @classmethod
    def serializer(cls, instance):
        result = super().serializer(instance)

        result.update(
            name=instance.name,
            abbreviation=instance.abbreviation
        )

        return result


class CitySerializer(BaseSerialization):
    _model = City
   
    @classmethod
    def serializer(cls, instance):
        result = super().serializer(instance)

        result.update(
            name=instance.name,
            state=StateSerializer.serializer(instance.state)
            #state_name=instance.state.name,
            #state_abbreviation=instance.state.abbreviation
        )

        return result