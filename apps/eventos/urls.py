from django.urls import path
from .views import crearEvento,listarEvento

urlpatterns = [
    path('crear_evento/',crearEvento, name = 'crear_evento'),
    path('listar_evento/',listarEvento, name = 'listar_evento')
]