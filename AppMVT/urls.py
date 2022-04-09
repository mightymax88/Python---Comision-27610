from django.urls import path, include
from AppMVT.views import probandoTemplate
from AppMVT import views

urlpatterns = [
    path('probandoTemplate/',probandoTemplate),
    path('', views.inicio),
    path('cursos', views.cursos),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
]