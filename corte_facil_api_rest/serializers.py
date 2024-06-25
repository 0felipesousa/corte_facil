from rest_framework import serializers
from .models import Service, HoursScheduling, Scheduling, SchedulingHistoric, Client, Barber, BarberShop

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class HoursSchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoursScheduling
        fields = '__all__'

class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = '__all__'

class SchedulingHistoricSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedulingHistoric
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = '__all__'

class BarberShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarberShop
        fields = '__all__'

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = ['id', 'name', 'email', 'password', 'phone', 'barberShop', 'available', 'created_at', 'updated_at']
        extra_kwargs = {
            'barberShop': {'required': False},
        }