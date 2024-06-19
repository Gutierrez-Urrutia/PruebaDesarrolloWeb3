from django.db import models

# Create your models here.

# Commented code
# class Cliente(models.Model):
#     
#     nombre = models.CharField(max_length=100)
#     apellido= models.CharField(max_length=100)
#     rut = models.CharField(max_length=12)
#     email = models.EmailField(primary_key = True, max_length=100)
#     telefono = models.CharField(max_length=20)
#     direccion = models.CharField(max_length=200, null=True, blank=True)
#     pais = models.CharField(max_length=50)
#     region = models.CharField(max_length=50)
#     comuna = models.CharField(max_length=50)
#     password = models.CharField(max_length=20)
# 
#     def __str__(self):
#         return self.nombre

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id_pais} - {self.nombre_pais}"
    
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_pais} - {self.id_region} - {self.nombre_region}"
    
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_region} - {self.id_comuna} - {self.nombre_comuna}"
    

