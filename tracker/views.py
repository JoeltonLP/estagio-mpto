import json

from django.shortcuts import render
from django.http.response import HttpResponse
from .models import State


def state_index(request):
    query = State.objects.all()
    response = HttpResponse()

    if query.exists():
        response.status_code = 200
    else:
        response.status_code = 404

    return response
