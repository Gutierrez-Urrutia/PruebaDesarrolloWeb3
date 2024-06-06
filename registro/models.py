from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key = True, max_length=12)
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    id_ciudad = models.CharField(max_length=10)
    id_pais = models.CharField(max_length=10)
    id_comuna = models.CharField(max_length=10)
    codigo_postal = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    id_pais = models.CharField(primary_key = True, max_length=10)
    nombre_pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_pais

class Region(models.Model):
    id_region = models.CharField(primary_key = True, max_length=10)
    nombre_region = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    id_comuna = models.CharField(primary_key = True, max_length=10)
    nombre_comuna = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombre_comuna
    

