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
    result = {}

    try:
        result = StateSerializer.serializer(
            State.objects.get(id=pk)
        )
    except State.DoesNotExist:
        status = 404
        result = {
            'Message': f'O item com a id igual a {pk} nao existe na base de dados'
        }

    return HttpResponse(
        status=status,
        content_type='application/json',
        content=json.dumps(result)
    )


def state_delete_by_pk(request, pk):
    status = 200
    result = {}
    try:
        State.objects.get(id=pk).delete()
        status = 204
        result = None
    except State.DoesNotExist:
        status = 404
        result = {
            'Message': f'pk {pk} nao existe na base de dados'
        }
    except Exception as e:
        result = {
            'Message': str(e)
        }
    return HttpResponse(
        status=status,
        content_type='application/json',
        content=json.dumps(result) if not result else None
    )


def state_update_by_pk(request, pk):
    status = 200
    result = {}
    try:
        with transaction.atomic():
            state = State.objects.get(id=pk)
            data = json.loads(request.body)

            for key, value in data.items():
                setattr(state, key, value)

            state.save()
            result = StateSerializer.serializer(state)
    except State.DoesNotExist:
        status = 404
        result = {
            'Message': f'pk {pk} nao existe na base de dados'
        }
    except Exception as e:
        status = 400
        result = {
            'Message': str(e)
        }
    return HttpResponse(
        status=status,
        content_type='application/json',
        content=json.dumps(result) if result else ''
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
    elif request.method == 'DELETE':
        return state_delete_by_pk(request, pk)
    elif request.method == 'PUT':
        return state_update_by_pk(request, pk)
    else:
        return HttpResponse(status=501)
