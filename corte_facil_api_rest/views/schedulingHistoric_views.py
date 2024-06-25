from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from corte_facil_api_rest.models import SchedulingHistoric
from corte_facil_api_rest.serializers import SchedulingHistoricSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    responses={200: SchedulingHistoricSerializer(many=True)}
)
@api_view(['GET'])
def get_scheduling_historic(request):
    if request.method == 'GET':
        scheduling_historic = SchedulingHistoric.objects.all()
        serializer = SchedulingHistoricSerializer(scheduling_historic, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=SchedulingHistoricSerializer,
    responses={201: SchedulingHistoricSerializer, 400: 'Bad Request'}
)
@api_view(['POST'])
def create_scheduling_historic(request):
    if request.method == 'POST':
        serializer = SchedulingHistoricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do SchedulingHistoric", type=openapi.TYPE_INTEGER)
    ],
    request_body=SchedulingHistoricSerializer,
    responses={200: SchedulingHistoricSerializer, 400: 'Bad Request', 404: 'Not Found'}
)
@api_view(['PUT'])
def update_scheduling_historic(request, pk):
    try:
        scheduling_historic = SchedulingHistoric.objects.get(pk=pk)
    except SchedulingHistoric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SchedulingHistoricSerializer(scheduling_historic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do SchedulingHistoric", type=openapi.TYPE_INTEGER)
    ],
    responses={204: 'No Content', 404: 'Not Found'}
)
@api_view(['DELETE'])
def delete_scheduling_historic(request, pk):
    try:
        scheduling_historic = SchedulingHistoric.objects.get(pk=pk)
    except SchedulingHistoric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        scheduling_historic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
