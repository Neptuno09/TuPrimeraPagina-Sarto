from django.shortcuts import render, redirect
from .forms import EstudianteForm
from .models import Estudiante
from django.urls import reverse
from django.http import HttpResponseRedirect

def registrar_estudianteform(request):
    if request.method == 'POST':
            form = EstudianteForm(request.POST)
            print(form)
            if form.is_valid:
                informacion = form.cleaned_data
                estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                                         edad=informacion['edad'],email=informacion['email']) 
                estudiante.save()
                return HttpResponseRedirect(reverse('success'))
    else: 
        form= EstudianteForm()
        return render(request, "estudianteform.html", {"form":form})