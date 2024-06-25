from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from corte_facil_api_rest.models import Client
from corte_facil_api_rest.serializers import ClientSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    responses={200: ClientSerializer(many=True)}
)
@api_view(['GET'])
def get_client(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=ClientSerializer,
    responses={201: ClientSerializer, 400: 'Bad Request'}
)
@api_view(['POST'])
def create_client(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do Client", type=openapi.TYPE_INTEGER)
    ],
    request_body=ClientSerializer,
    responses={200: ClientSerializer, 400: 'Bad Request', 404: 'Not Found'}
)
@api_view(['PUT'])
def update_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do Client", type=openapi.TYPE_INTEGER)
    ],
    responses={204: 'No Content', 404: 'Not Found'}
)
@api_view(['DELETE'])
def delete_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
