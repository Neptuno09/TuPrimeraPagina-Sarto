from django.db import models

class Entrega(models.Model):
    nombre= models.CharField(max_length=30)
    nombre_alumno= models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)  
    entregado = models.BooleanField()
    
    def __str__(self):
        return self.nombre