from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca", views.acerca_de, name="acerca"),
    path("cursos", views.cursos, name="cursos"),
    path("servicio-dolar", views.servicio_dolar, name="dolar"),
    path("dolar-visto", views.dolar_visto, name="dolar_visto"),
    path("aeropuertos", views.aeropuertos, name="aeropuertos"),
    path("servicio-aeropuertos", views.servicio_aeropuertos,
         name="servicio_aeropuertos"),
]
