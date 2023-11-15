from django.shortcuts import render, redirect
from .models import Profesor
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
def registro_profesor(request):
    return render(request,"profesorform.html")
def registrar_profesorform(request):
    if request.method == 'POST':
            miFormulario = ProfesorForm(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                                     edad=informacion['edad'],email=informacion['email']) 
                profesor.save()
                return HttpResponseRedirect(reverse('success'))
    else: 
        miFormulario= ProfesorForm()
        return render(request, "registroprofe.html", {"miFormulario":miFormulario})
    
def buscarprof(request):
    if request.method == 'POST':
        form = BuscarProfesorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            profesor = Profesor.objects.filter(nombre__icontains=nombre).first()

            if profesor:
                return render(request, "resultados_busqueda", {'profesor': profesor})
            else:
                mensaje_error = f"No se encontró ningún profesor con el nombre '{nombre}'."
                return render(request, 'buscarprof.html', {'form': form, 'mensaje_error': mensaje_error})
    else:
        form = BuscarProfesorForm()

    return render(request, 'buscarprof.html', {'form': form})