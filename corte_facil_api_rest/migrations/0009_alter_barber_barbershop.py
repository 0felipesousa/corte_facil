# Generated by Django 5.0.6 on 2025-01-20 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corte_facil_api_rest', '0008_alter_barber_barbershop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='barberShop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corte_facil_api_rest.barbershop'),
        ),
    ]
