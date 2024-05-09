from django.db import models
from django.utils import timezone

class Service(models.Model):
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class HoursScheduling(models.Model):
    BARBER_DAY_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terça', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sábado', 'Sábado'),
    ]
    barber = models.ForeignKey('Barber', on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    day = models.CharField(max_length=10, choices=BARBER_DAY_CHOICES)
    status = models.BooleanField(default=False)

class Scheduling(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    hour = models.ForeignKey('HoursScheduling', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class SchedulingHistoric(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    hour = models.ForeignKey('HoursScheduling', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    done = models.BooleanField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    login = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

class Barber(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    barber_shop = models.ForeignKey('BarberShop', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

class BarberShop(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField()
    address_id = models.IntegerField()  # You might want to use a ForeignKey to an Address model
    owner = models.ForeignKey('Barber', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
