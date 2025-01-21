# Generated by Django 5.0.6 on 2025-01-20 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corte_facil_api_rest', '0006_rename_barber_shop_barber_barbershop_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='barberShop',
            field=models.ForeignKey(default='Nulo', on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.barbershop'),
        ),
        migrations.AlterField(
            model_name='barbershop',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corte_facil_api_rest.barber'),
        ),
    ]
