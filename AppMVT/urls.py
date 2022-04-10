from django.urls import path, include
from AppMVT.views import probandoTemplate
from AppMVT import views

urlpatterns = [
    path('probandoTemplate/',probandoTemplate),
    path('', views.inicio, name = "Inicio"),
    path('cursos', views.cursos, name = "Cursos"),
    path('profesores', views.profesores, name = "Profesores"),
    path('estudiantes', views.estudiantes, name = "Estudiantes"),
    path('entregables', views.entregables, name = "Entregables"),
    path('cursoFormulario', views.cursoFormulario, name = "CursoFormulario"),
    path('profesorFormulario', views.profesorFormulario, name = "ProfesorFormulario"),
    path('busquedaCamada', views.busquedaCamada, name = "BusquedaCamada"),
    path('buscar', views.buscar),
    path('estudianteFormulario', views.estudianteFormulario, name = "EstudianteFormulario"),
    path('entregableFormulario', views.entregableFormulario, name = "EntregableFormulario"),
]