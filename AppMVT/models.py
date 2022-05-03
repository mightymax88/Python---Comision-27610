from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Blog(models.Model):
    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 30)
    cuerpo = models.CharField(max_length = 300)
    cuerpo = RichTextField()
    autor = models.CharField(max_length = 30)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to = 'blogs/', null = True, blank = True)
    def __str__(self):
        return f"Título: {self.titulo} - Autor {self.autor}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-mail {self.email}"

class Entregable(models.Model):
    nombre = models.CharField(max_length = 30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha Entrega {self.fechaDeEntrega} - Entregado {self.entregado}"

class ClasesQueNecesitaLogin(LoginRequiredMixin):
    Entregable

class Avatar(models.Model):
    #Vinculo con el usuario
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    #Subcarpeta avatares de media
    imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)

class Message(models.Model):
    mensaje = models.CharField(max_length = 500)
    autor = models.CharField(max_length = 30)
    fecha = models.DateField()
    def __str__(self):
        return f"Autor: {self.autor} - Fecha {self.fecha}"