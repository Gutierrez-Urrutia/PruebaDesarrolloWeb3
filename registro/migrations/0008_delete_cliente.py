# Generated by Django 5.0.6 on 2024-06-14 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0007_alter_cliente_direccion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
