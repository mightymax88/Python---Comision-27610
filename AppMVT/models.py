from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length = 30)
    dni = models.IntegerField()
    fechaNac = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length = 30)
    clase = models.CharField(max_length = 30)

class Curso(models.Model):
    nombre = models.CharField(max_length = 30)
    clase = models.CharField(max_length = 30)