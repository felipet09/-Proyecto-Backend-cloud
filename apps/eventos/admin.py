from django.contrib import admin
from .models import Evento,Categoria, Tipo

# Register your models here.
admin.site.register(Evento)
admin.site.register(Categoria)
admin.site.register(Tipo)