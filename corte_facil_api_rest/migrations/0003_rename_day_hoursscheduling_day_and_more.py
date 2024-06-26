# Generated by Django 5.0.6 on 2024-05-28 16:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corte_facil_api_rest', '0002_barber_barbershop_client_hoursscheduling_scheduling_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hoursscheduling',
            old_name='day',
            new_name='Day',
        ),
        migrations.RenameField(
            model_name='hoursscheduling',
            old_name='date',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='hoursscheduling',
            old_name='hour',
            new_name='hora',
        ),
        migrations.AddField(
            model_name='barber',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterModelTable(
            name='hoursscheduling',
            table='hoursScheduling',
        ),
        migrations.AlterModelTable(
            name='service',
            table='services',
        ),
    ]
