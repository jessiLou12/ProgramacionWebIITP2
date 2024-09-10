from django.urls import path
from .views import MensajeDeleteView, CrearMensajeView, ListaViewMensajes

#aca agregar vistas

app_name = 'mensajes'

urlpatterns = [
    path('',ListaViewMensajes.as_view(),name='lista_mensaje'),
    path('eliminar/<int:pk>/', MensajeDeleteView.as_view(), name='eliminar_mensaje'),
    path('crear/', CrearMensajeView.as_view(), name='crear_mensaje'),

    ]




