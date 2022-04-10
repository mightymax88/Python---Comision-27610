from django import forms

class CursoFormulario(forms.Form):
    #Especifico los campos
    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    #Especifico los campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):
    #Especifico los campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    #Especifico los campos
    nombre = forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()