
class BaseSerializer:

    _model = None

    @classmethod
    def Model(cls):
        print('--*', cls._model)
        return cls._model 

    @classmethod
    def encode(cls, instance):
        return {
            'pk': instance.pk,
            'description': str(instance),
        }

    @classmethod
    def decode(cls, data):
        return cls._model(**data)
