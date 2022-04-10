from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length = 30)
    dni = models.IntegerField()
    fechaNac = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()
    profesion = models.CharField(max_length = 30)

class Curso(models.Model):
    nombre = models.CharField(max_length = 30)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()

class Entregable(models.Model):
    nombre = models.CharField(max_length = 30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()