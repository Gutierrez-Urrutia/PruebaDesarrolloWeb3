# Generated by Django 5.0.6 on 2024-06-14 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_rename_region_comuna_id_region_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nombre_usuario',
        ),
    ]
