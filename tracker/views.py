
from helprs import restfy

from .serializers import (
    StateSerializer, 
    CitySerializer
)


city_index, city_by_id = restfy.make_rest(CitySerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
