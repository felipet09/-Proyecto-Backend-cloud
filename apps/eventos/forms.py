from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre','lugar','direccion','fecha_inicio','fecha_final','id_categoria']