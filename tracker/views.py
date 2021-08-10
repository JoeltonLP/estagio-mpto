
import json
from helprs import restfy

from tracker.models import PackageContainer

from django.http.response import HttpResponse, HttpResponseNotAllowed

from .serializers import (
    StateSerializer, 
    CitySerializer,
    PersonSerializer,
    NaturalPersonSerializer,
    LegalPersonSerializer,
    PackageContainerSerilizer,
    LogTraceSerializer
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


def package_container_log_trace_register(request, unique_identify):

    status = 501
    content = None

    data = json.loads(request.body)

    print('--', unique_identify)
    
    try:

        package = PackageContainer.objects.get(unique_identify=unique_identify)
        print('--', data)
        log_trace = LogTraceSerializer.decode(data)
        package.logs.add(log_trace)

        status = 501

        content = json.dumps(
            LogTraceSerializer.encode(log_trace)
        )
        

    except PackageContainer.DoesNotExist:
        
        content = json.dumps({
            'message': f'pacote {unique_identify} não encontrado'
        })
    
    except Exception as e:
        
        status = 400
        content = json.dumps({
            'message': str(e)
        })


    return HttpResponse(
        status=status,
        content_type='application/json',
        content=content
    )


def package_container_register_log_trace_list(request, unique_identify):
    pass


def package_container_log_trace(request, unique_identify):
    
    status = 501
    if request.method == 'GET':
        return package_container_register_log_trace_list(request, unique_identify)
    elif request.method == 'POST':
        return package_container_log_trace_register(request, unique_identify)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
    