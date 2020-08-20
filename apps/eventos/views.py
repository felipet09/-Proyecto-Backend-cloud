from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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

def editarEvento(request,id):
    evento_form = None
    error = None
    try:
        evento = get_evento.objects.get(id = id)
        if request.method == 'GET':
            evento_form = EventoForm(instance = evento)
        else:
            evento_form = EventoForm(request.POST, instance = evento)
            if evento_form.is_valid():
                evento_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request,'eventos/crear_evento.html',{'evento_form':evento_form,'error':error})

def eliminarEvento(request,id):
    evento = get_evento.objects.get(id = id)
    if request.method == 'POST':
        evento.delete()
        return redirect('eventos:listar_evento')
    return render(request,'eventos/eliminar_evento.html',{'evento':evento})