from django.shortcuts import render
import sqlite3
from AppMVT.models import Blog, Message, Avatar
from AppMVT.forms import UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})

def about(request):
    return render(request, "AppCoder/about.html")

def enDesarrollo(request):
    return render(request, "AppCoder/enDesarrollo.html")

#CLASES BASADAS EN VISTAS
class PagesList(ListView):
    model = Blog
    template_name = "AppCoder/pages_list.html"

class PagesDetalle(DetailView):
    model = Blog
    template_name = "AppCoder/pages_detalle.html"

class PagesCreacion(CreateView):
    model = Blog
    success_url = "/AppMVT/pages/list"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class PagesUpdate(UpdateView):
    model = Blog
    success_url = "/AppMVT/pages/list"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class PagesDelete(DeleteView):
    model = Blog
    success_url = "/AppMVT/pages/list"

#CLASES BASADAS EN VISTAS
class MessageList(ListView):
    model = Message
    template_name = "AppCoder/messages_list.html"

class MessageCreacion(CreateView):
    model = Message
    success_url = "messages/list"
    fields = ['mensaje', 'autor', 'fecha']

#LOGIN
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            if user is not None:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {'form':form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario Creado"})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, "AppCoder/registro.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario": usuario})