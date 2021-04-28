from django.urls import path
from .views import state_index

from django.urls import path
from .views import (
    state_index, 
    state_by_pk,
    city_index,
    city_by_id
)

urlpatterns = [
    path('states', state_index),
    path('states/<int:pk>', state_by_pk),
    path('cities', city_index),
    path('cities/<int:id>', city_by_id)
]