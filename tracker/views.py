import json

from django.http.response import HttpResponse
from django.db import transaction

from .models import State
from .serialization import StateSerializer


def state_list(request):
    response = None

    query = State.objects.all()
    response = HttpResponse()
    response.status_code = 501

    if query.exists():
        response = HttpResponse(
            content_type='application/json',
            content=json.dumps([
                StateSerializer.serializer(state) for state in query
            ])
        )
    else:
        response.status_code = 404
    return response


def state_create(request):

    try:
        with transaction.atomic():
            data = json.loads(request.body)
            state = StateSerializer.deserializer(data)
            state.save()

            response = HttpResponse(
                content=json.dumps(
                    StateSerializer.serializer(state)
                ),
                status=201
            )
    except Exception as e:
        response = HttpResponse(
            content=json.dumps({
                'message': str(e)
            }),
            status=400
        )

    return response


def state_get_by_pk(request, pk):
    status = 200
    result  = {}

    try:
       result =  StateSerializer.serializer(
            State.objects.get(id=pk)
        )
    except State.DoesNotExist:
        status = 404
        result = {
            'Message': f'the  item with  pk {pk} not exists'
        }
       
    return HttpResponse(
        status=status,
        content_type='application/json',
        content=json.dumps(result)
    )


def state_index(request):
    response = None
    if request.method == 'GET':
        response = state_list(request)
    elif request.method == 'POST':
        response = state_create(request)
    return response


def state_by_pk(request, pk):
    if request.method == 'GET':

        return state_get_by_pk(request, pk)
    else:
        return HttpResponse(status=501)
