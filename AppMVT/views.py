from django.shortcuts import render
import datetime
from django.template import Context, Template
from django.template import loader
from django.http import HttpResponse
import sqlite3

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