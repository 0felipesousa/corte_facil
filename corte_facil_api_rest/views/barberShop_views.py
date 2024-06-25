from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from corte_facil_api_rest.models import BarberShop
from corte_facil_api_rest.serializers import BarberShopSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    responses={200: BarberShopSerializer(many=True)}
)
@api_view(['GET'])
def get_barber_shop(request):
    if request.method == 'GET':
        barber_shops = BarberShop.objects.all()
        serializer = BarberShopSerializer(barber_shops, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=BarberShopSerializer,
    responses={201: BarberShopSerializer, 400: 'Bad Request'}
)
@api_view(['POST'])
def create_barber_shop(request):
    if request.method == 'POST':
        serializer = BarberShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do BarberShop", type=openapi.TYPE_INTEGER)
    ],
    request_body=BarberShopSerializer,
    responses={200: BarberShopSerializer, 400: 'Bad Request', 404: 'Not Found'}
)
@api_view(['PUT'])
def update_barber_shop(request, pk):
    try:
        barber_shop = BarberShop.objects.get(pk=pk)
    except BarberShop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BarberShopSerializer(barber_shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='delete',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID do BarberShop", type=openapi.TYPE_INTEGER)
    ],
    responses={204: 'No Content', 404: 'Not Found'}
)
@api_view(['DELETE'])
def delete_barber_shop(request, pk):
    try:
        barber_shop = BarberShop.objects.get(pk=pk)
    except BarberShop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        barber_shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
