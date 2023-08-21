from django.db import models
from django.contrib.auth.models import User



class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"

# Create your models here.

class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=30)
    apellido_empleado = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"nombre: {self.nombre_empleado} - apellido: {self.apellido_empleado} - email: {self.email}"
    
    
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=30)
    apellido_cliente = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"nombre: {self.nombre_cliente} - apellido: {self.apellido_cliente} - email: {self.email}"
    
    
class Sector(models.Model):
    nombre_empleado = models.CharField(max_length=30)
    zona_trabajo = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre_empleado} - Area: {self.zona_trabajo} "
    
    
class Encargado(models.Model):
    nombre_encargado = models.CharField(max_length=30)
    apellido_encargado = models.CharField(max_length=30)
    email = models.EmailField()
    sector = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre_encargado} - Apellido: {self.apellido_encargado} - E-Mail: {self.email} - Sector: {self.sector}"
    

