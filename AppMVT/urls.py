from django.urls import path, include
from AppMVT import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('about', views.about, name = 'About'),
    #Clases basadas en vistas
    path('pages/list', views.PagesList.as_view(), name = 'PagesList'),
    path(r'^(?P<pk>\d+)$', views.PagesDetalle.as_view(), name = 'Detail'),
    path(r'^nuevo$', views.PagesCreacion.as_view(), name = 'New'),
    path(r'editar/^(?P<pk>\d+)$', views.PagesUpdate.as_view(), name = 'Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PagesDelete.as_view(), name = 'Delete'),
    #Enlaces de login y registro
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name = "AppCoder/logout.html"), name = 'Logout'),
    #Enlace a editar perfil de usuario
    path('editarPerfil', views.editarPerfil, name = 'EditarPerfil'),
    #Enlace a página en desarrollo
    path('enDesarrollo', views.enDesarrollo, name = 'Desarrollo'),
    #Clases basadas en vistas
    path('messages/list', views.MessageList.as_view(), name = 'MessageList'),
    path(r'^nuevom$', views.MessageCreacion.as_view(), name = 'MessageNew'),
]