# Generated by Django 4.2 on 2023-04-08 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_comprador_vehiculo_vendedor_delete_animal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendedor',
            old_name='cantidad_ventas',
            new_name='meses_de_contrato',
        ),
    ]
