from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido

