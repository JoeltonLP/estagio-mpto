from django.urls import path
from .views import state_index

from django.urls import path
from .views import (
    state_index, 
    state_by_id,
    city_index,
    city_by_id,
    natural_person_index,
    natural_person_by_id,
    legal_person_index,
    legal_person_by_id,
    person_index,
    person_by_id
)

urlpatterns = [
    path('states', state_index),
    path('states/<int:id>', state_by_id),
    path('cities', city_index),
    path('cities/<int:id>', city_by_id),
    path('natural-persons', natural_person_index),
    path('persons', person_index),
    path('persons/<int:id>', person_by_id),
    path('natural-persons/<int:id>', natural_person_by_id),
    path('legal-persons', legal_person_index),
    path('legal-persons/<int:id>', legal_person_by_id)
]
