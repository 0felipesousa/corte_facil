from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from corte_facil_api_rest.models import HoursScheduling
from corte_facil_api_rest.serializers import HoursSchedulingSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    responses={200: HoursSchedulingSerializer(many=True)}
)
@api_view(['GET'])
def get_hours_scheduling(request):
    if request.method == 'GET':
        hours_scheduling = HoursScheduling.objects.all()
        serializer = HoursSchedulingSerializer(hours_scheduling, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=HoursSchedulingSerializer,
    responses={201: HoursSchedulingSerializer, 400: 'Bad Request'}
)
@api_view(['POST'])
def create_hours_scheduling(request):
    if request.method == 'POST':
        serializer = HoursSchedulingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do HoursScheduling", type=openapi.TYPE_INTEGER)
    ],
    request_body=HoursSchedulingSerializer,
    responses={200: HoursSchedulingSerializer, 400: 'Bad Request', 404: 'Not Found'}
)
@api_view(['PUT'])
def update_hours_scheduling(request, pk):
    try:
        hours_scheduling = HoursScheduling.objects.get(pk=pk)
    except HoursScheduling.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = HoursSchedulingSerializer(hours_scheduling, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do HoursScheduling", type=openapi.TYPE_INTEGER)
    ],
    responses={204: 'No Content', 404: 'Not Found'}
)
@api_view(['DELETE'])
def delete_hours_scheduling(request, pk):
    try:
        hours_scheduling = HoursScheduling.objects.get(pk=pk)
    except HoursScheduling.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        hours_scheduling.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
