from django.shortcuts import render
import datetime
from django.template import Context, Template
from django.template import loader
from django.http import HttpResponse
import sqlite3
from AppMVT.models import Curso, Entregable, Estudiante, Profesor
from AppMVT.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario

# Create your views here.
def probandoTemplate(self):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM AppMVT_familiar")
    result = cur.fetchall()
    dia = datetime.datetime.now()
    diccionario = {"db":result, "fecha":dia}
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    con.close()
    return HttpResponse(documento)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM AppMVT_curso")
    result = cur.fetchall()
    dia = datetime.datetime.now()
    diccionario = {"db":result, "fecha":dia}
    plantilla = loader.get_template("AppCoder/cursos.html")
    documento = plantilla.render(diccionario)
    con.close()
    return HttpResponse(documento)

def profesores(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM AppMVT_profesor")
    result = cur.fetchall()
    dia = datetime.datetime.now()
    diccionario = {"db":result, "fecha":dia}
    plantilla = loader.get_template("AppCoder/profesores.html")
    documento = plantilla.render(diccionario)
    con.close()
    return HttpResponse(documento)

def estudiantes(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM AppMVT_estudiante")
    result = cur.fetchall()
    dia = datetime.datetime.now()
    diccionario = {"db":result, "fecha":dia}
    plantilla = loader.get_template("AppCoder/estudiantes.html")
    documento = plantilla.render(diccionario)
    con.close()
    return HttpResponse(documento)

def entregables(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM AppMVT_entregable")
    result = cur.fetchall()
    dia = datetime.datetime.now()
    diccionario = {"db":result, "fecha":dia}
    plantilla = loader.get_template("AppCoder/entregables.html")
    documento = plantilla.render(diccionario)
    con.close()
    return HttpResponse(documento)

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso= Curso(nombre = informacion['curso'], camada = informacion['camada'])
            curso.save()
            return render(request, "inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor= Profesor(nombre = informacion['nombre'], apellido = informacion['apellido'],
                email = informacion['email'], profesion = informacion['profesion'])
            profesor.save()
            return render(request, "inicio.html")
    else:
        miFormulario = ProfesorFormulario()
    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})

def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante= Estudiante(nombre = informacion['nombre'], apellido = informacion['apellido'],
                email = informacion['email'])
            estudiante.save()
            return render(request, "inicio.html")
    else:
        miFormulario = EstudianteFormulario()
    return render(request, "AppCoder/estudianteFormulario.html", {"miFormulario":miFormulario})

def entregableFormulario(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable= Entregable(nombre = informacion['nombre'], fechaDeEntrega = informacion['fechaDeEntrega'],
                entregado = informacion['entregado'])
            entregable.save()
            return render(request, "inicio.html")
    else:
        miFormulario = EntregableFormulario()
    return render(request, "AppCoder/entregableFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada)
        return render(request, "resultadosBusqueda.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)