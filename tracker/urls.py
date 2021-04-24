from django.urls import path
from .views import state_index, state_by_pk

urlpatterns = [
    path('states', state_index),
    path('states/<int:pk>', state_by_pk)
]
