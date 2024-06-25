from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from corte_facil_api_rest.models import Service
from corte_facil_api_rest.serializers import ServiceSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import json
@swagger_auto_schema(
    method='get',
    responses={200: ServiceSerializer(many=True)}
)
@api_view(['GET'])
def get_service(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=ServiceSerializer,
    responses={201: ServiceSerializer(), 400: 'Bad Request'}
)
@api_view(['POST'])
def create_service(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID of the service", type=openapi.TYPE_INTEGER)
    ],
    request_body=ServiceSerializer,
    responses={200: ServiceSerializer(), 400: 'Bad Request', 404: 'Not Found'}
)
@api_view(['PUT'])
def update_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID of the service", type=openapi.TYPE_INTEGER)
    ],
    responses={204: 'No Content', 404: 'Not Found'}
)
@api_view(['DELETE'])
def delete_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
