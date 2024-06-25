from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

import json
@swagger_auto_schema(
    method='get',
    responses={200: ServiceSerializer(many=True)},
    operation_description="Obter todos os serviços"
)
@api_view(['GET'])
def get_service(request):
    if request.method == 'GET':
        services = Service.objects.all()

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
