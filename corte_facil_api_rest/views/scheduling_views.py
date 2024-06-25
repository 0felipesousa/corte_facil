from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from corte_facil_api_rest.models import Scheduling
from corte_facil_api_rest.serializers import SchedulingSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    responses={200: SchedulingSerializer(many=True)}
)
@api_view(['GET'])
def get_scheduling(request):
    if request.method == 'GET':
        schedulings = Scheduling.objects.all()
        serializer = SchedulingSerializer(schedulings, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=SchedulingSerializer,
    responses={201: SchedulingSerializer, 400: 'Bad Request'}
)
@api_view(['POST'])
def create_scheduling(request):
    if request.method == 'POST':
        serializer = SchedulingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do Scheduling", type=openapi.TYPE_INTEGER)
    ],
    request_body=SchedulingSerializer,
    responses={200: SchedulingSerializer, 400: 'Bad Request', 404: 'Not Found'}
)
@api_view(['PUT'])
def update_scheduling(request, pk):
    try:
        scheduling = Scheduling.objects.get(pk=pk)
    except Scheduling.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SchedulingSerializer(scheduling, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do Scheduling", type=openapi.TYPE_INTEGER)
    ],
    responses={204: 'No Content', 404: 'Not Found'}
)
@api_view(['DELETE'])
def delete_scheduling(request, pk):
    try:
        scheduling = Scheduling.objects.get(pk=pk)
    except Scheduling.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        scheduling.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
