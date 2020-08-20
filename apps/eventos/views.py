from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Evento as get_evento

# Create your views here.
def Evento(request):
    return render(request,'index.html')

def crearEvento(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        if evento_form.is_valid():
            evento_form.save()
            return redirect('index')
    else:
        evento_form = EventoForm()
    return render(request,'eventos/crear_evento.html',{'evento_form':evento_form})

def listarEvento(request):
    eventos = get_evento.objects.all()
    return render(request,'eventos/listar_evento.html',{'eventos':eventos})