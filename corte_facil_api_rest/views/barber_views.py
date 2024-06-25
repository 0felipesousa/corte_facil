from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from corte_facil_api_rest import serializers
from corte_facil_api_rest.models import Barber
from corte_facil_api_rest.serializers import BarberSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    responses={200: BarberSerializer(many=True)},
)
@api_view(['GET'])
def get_barber(request):
    if request.method == 'GET':
        barbers = Barber.objects.all()
        serializer = BarberSerializer(barbers, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=BarberSerializer,
    responses={201: BarberSerializer, 400: 'Bad Request'},
)


@api_view(['POST'])
def create_barber(request):
    if request.method == 'POST':
        serializer = BarberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    methods=['put', 'patch'],
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do Barber", type=openapi.TYPE_INTEGER)
    ],
    request_body=BarberSerializer,
    responses={200: BarberSerializer, 400: 'Bad Request', 404: 'Not Found'},
)

@api_view(['PUT', 'PATCH'])
def update_barber(request, pk):
    try:
        barber = Barber.objects.get(pk=pk)
    except Barber.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = BarberSerializer(barber, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do Barber", type=openapi.TYPE_INTEGER)
    ],
    responses={204: 'No Content', 404: 'Not Found'},
)
@api_view(['DELETE'])
def delete_barber(request, pk):
    try:
        barber = Barber.objects.get(pk=pk)
    except Barber.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        barber.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
