from django.shortcuts import render
import datetime
from django.template import Context, Template
from django.template import loader
from django.http import HttpResponse
import sqlite3
from AppMVT.models import Curso, Profesor
from AppMVT.forms import CursoFormulario, ProfesorFormulario

# Create your views here.
def probandoTemplate(self):
    con = sqlite3.connect("/Volumes/GoogleDrive-109720198790235587340/Mi unidad/Cursos/CODERHOUSE/Python/Proyecto 01/MVT_Maxi/db.sqlite3")
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
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso= Curso(nombre = informacion['curso'], camada = informacion['camada'])
            curso.save()
            return render(request, "AppMVT/inicio.html")
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
            return render(request, "AppMVT/inicio.html")
    else:
        miFormulario = ProfesorFormulario()
    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada_icontains=camada)
        return render(request, "AppMVT/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)