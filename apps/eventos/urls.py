from django.urls import path
from .views import crearEvento,listarEvento,editarEvento,eliminarEvento

urlpatterns = [
    path('crear_evento/',crearEvento, name = 'crear_evento'),
    path('listar_evento/',listarEvento, name = 'listar_evento'),
    path('editar_evento/<int:id>',editarEvento, name = 'editar_evento'),
    path('eliminar_evento/<int:id>',eliminarEvento, name = 'eliminar_evento')
]