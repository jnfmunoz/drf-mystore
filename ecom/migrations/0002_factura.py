# Generated by Django 5.0 on 2023-12-12 20:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('fecha_vencimento', models.DateField()),
                ('total_factura', models.FloatField()),
                ('transaccion_id', models.CharField(blank=True, max_length=50, null=True)),
                ('pagado', models.BooleanField(default=False)),
                ('fkCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='cliente')),
            ],
        ),
    ]
