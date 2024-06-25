from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Service
from .views.barberShop_views import get_barber_shop, create_barber_shop, update_barber_shop, delete_barber_shop
from .views.barber_views import get_barber, create_barber, update_barber, delete_barber
from .views.client_views import get_client, update_client, delete_client, create_client
from .views.hoursScheduling_views import get_hours_scheduling, create_hours_scheduling, update_hours_scheduling, \
    delete_hours_scheduling
from .views.schedulingHistoric_views import get_scheduling_historic, create_scheduling_historic, \
    update_scheduling_historic, delete_scheduling_historic
from .views.scheduling_views import get_scheduling, create_scheduling, update_scheduling, delete_scheduling

from .views.services_views import get_service, create_service, update_service, delete_service

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('services/', get_service, name='get_service'),
    path('services/create/', create_service, name='create_service'),
    path('services/update/<int:pk>/', update_service, name='update_service'),
    path('services/delete/<int:pk>/', delete_service, name='delete_service'),

    path('hoursScheduling/', get_hours_scheduling, name='get_hours_scheduling'),
    path('hoursScheduling/create/', create_hours_scheduling, name='create_hours_scheduling'),
    path('hoursScheduling/update/<int:pk>/', update_hours_scheduling, name='update_hours_scheduling'),
    path('hoursScheduling/delete/<int:pk>/', delete_hours_scheduling, name='delete_hours_scheduling'),

    path('schedulingHistoric/', get_scheduling_historic, name='get_scheduling_historic'),
    path('schedulingHistoric/create/', create_scheduling_historic, name='create_scheduling_historic'),
    path('schedulingHistoric/update/<int:pk>/', update_scheduling_historic, name='update_scheduling_historic'),
    path('schedulingHistoric/delete/<int:pk>/', delete_scheduling_historic, name='delete_scheduling_historic'),

    path('scheduling/', get_scheduling, name='get_scheduling'),
    path('scheduling/create/', create_scheduling, name='create_scheduling'),
    path('scheduling/update/<int:pk>/', update_scheduling, name='update_scheduling'),
    path('scheduling/delete/<int:pk>/', delete_scheduling, name='delete_scheduling'),

    path('client/', get_client, name='get_client'),
    path('client/create/', create_client, name='create_client'),
    path('client/update/<int:pk>/', update_client, name='update_client'),
    path('client/delete/<int:pk>/', delete_client, name='delete_client'),

    path('barber/', get_barber, name='get_barber'),
    path('barber/create/', create_barber, name='create_barber'),
    path('barber/update/<int:pk>/', update_barber, name='update_barber'),
    path('barber/delete/<int:pk>/', delete_barber, name='delete_barber'),

    path('barberShop/', get_barber_shop, name='get_barber_shop'),
    path('barberShop/create/', create_barber_shop, name='create_barber_shop'),
    path('barberShop/update/<int:pk>/', update_barber_shop, name='update_barber_shop'),
    path('barberShop/delete/<int:pk>/', delete_barber_shop, name='delete_barber_shop'),


]

