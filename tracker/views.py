
from helprs import restfy

from .serializers import (
    StateSerializer, 
    CitySerializer,
    PersonSerializer,
    NaturalPersonSerializer,
    LegalPersonSerializer,
    PackageContainerSerilizer
)

person_index, person_by_id = restfy.make_rest(
    PersonSerializer,
    allow_list=True,
    allow_get=True,
    allow_create=False, 
    allow_update=False, 
    allow_delete=False
)

natural_person_index, natural_person_by_id = restfy.make_rest(
    NaturalPersonSerializer
)
legal_person_index, legal_person_by_id = restfy.make_rest(LegalPersonSerializer)
city_index, city_by_id = restfy.make_rest(CitySerializer)
state_index, state_by_id = restfy.make_rest(StateSerializer)
package_container_index, package_container_by_id = restfy.make_rest(PackageContainerSerilizer)
