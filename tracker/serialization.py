from .models import State


class BaseSerialization:

    _model = None

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
    _model = State

    @classmethod
    def serializer(cls, instance):
        result = super().serializer(instance)

        result.update(
            name=instance.name,
            abbreviation=instance.abbreviation
        )

        return result
