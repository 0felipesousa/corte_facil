from django.contrib import admin

from .models import Service, HoursScheduling, Scheduling, SchedulingHistoric, Client, Barber, BarberShop

admin.site.register(Service)
admin.site.register(HoursScheduling)
admin.site.register(Scheduling)
admin.site.register(SchedulingHistoric)
admin.site.register(Client)
admin.site.register(Barber)
admin.site.register(BarberShop)
