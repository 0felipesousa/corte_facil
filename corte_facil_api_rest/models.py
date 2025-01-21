from django.db import models
from django.utils import timezone

class Service(models.Model):
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'services'
    def __str__(self):
        return self.description

class HoursScheduling(models.Model):
    days = [
        ('segunda', 'Segunda-feira'),
        ('terça', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sábado', 'Sábado'),
    ]
    barber = models.ForeignKey('Barber', on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    day = models.CharField(max_length=20, choices=days, default="Today")
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'hoursScheduling'
    def __str__(self):
        return '__all__'

class Scheduling(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    hour = models.ForeignKey('HoursScheduling', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'corte_facil_api_rest_scheduling'

    def __str__(self):
        return f"{self.client} {self.service} {self.hour}"

class SchedulingHistoric(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    hour = models.ForeignKey('HoursScheduling', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    done = models.BooleanField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'corte_facil_api_rest_schedulinghistoric'
    def __str__(self):
        return '__all__'

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    login = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'corte_facil_api_rest_client'

    def __str__(self):
        return self.name

class Barber(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    barberShop = models.ForeignKey('BarberShop', on_delete=models.SET_NULL, null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'corte_facil_api_rest_barber'
    def __str__(self):
        return self.name


class BarberShop(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField()
    address_id = models.IntegerField()
    owner = models.ForeignKey('Barber', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'corte_facil_api_rest_barbershop'
    def __str__(self):
        return self.name