from django.urls import path
from .views import state_index

urlpatterns = [
    path('states', state_index)
]
