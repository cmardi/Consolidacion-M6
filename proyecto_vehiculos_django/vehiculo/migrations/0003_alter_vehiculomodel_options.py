# Generated by Django 4.2.17 on 2024-12-13 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_vehiculomodel_delete_vehiculo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodel',
            options={'permissions': (('visualizar_catalogo', 'Visualizar catálogo de Vehículos'),)},
        ),
    ]
