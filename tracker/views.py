
from helprs import restfy

from .serializers import (
    StateSerializer, 
    CitySerializer,
    PersonSerializer,
    NaturalPersonSerializer
)

natural_person_index, natural_person_by_id = restfy.make_rest(NaturalPersonSerializer)
city_index, city_by_id = restfy.make_rest(CitySerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
