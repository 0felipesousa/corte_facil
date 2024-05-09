# Generated by Django 5.0.6 on 2024-05-09 22:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corte_facil_api_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='BarberShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.IntegerField()),
                ('address_id', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.barber')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('login', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HoursScheduling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('day', models.CharField(choices=[('segunda', 'Segunda-feira'), ('terça', 'Terça-feira'), ('quarta', 'Quarta-feira'), ('quinta', 'Quinta-feira'), ('sexta', 'Sexta-feira'), ('sábado', 'Sábado')], max_length=10)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.client')),
            ],
        ),
        migrations.CreateModel(
            name='SchedulingHistoric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField()),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.client')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='barber',
            name='barber_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.barbershop'),
        ),
        migrations.AddField(
            model_name='hoursscheduling',
            name='barber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.barber'),
        ),
        migrations.AddField(
            model_name='scheduling',
            name='hour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.hoursscheduling'),
        ),
        migrations.AddField(
            model_name='schedulinghistoric',
            name='hour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.hoursscheduling'),
        ),
        migrations.AddField(
            model_name='schedulinghistoric',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.service'),
        ),
        migrations.AddField(
            model_name='scheduling',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corte_facil_api_rest.service'),
        ),
    ]
