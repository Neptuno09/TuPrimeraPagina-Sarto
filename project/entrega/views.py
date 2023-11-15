from django.shortcuts import render, redirect
from .forms import EntregaForm
from .models import Entrega
from django.urls import reverse
from django.http import HttpResponseRedirect

def registrar_entregaform(request):
    if request.method == 'POST':
            form = EntregaForm(request.POST)
            print(form)
            if form.is_valid:
                informacion = form.cleaned_data
                entrega = Entrega (nombre=informacion['nombre'],descripcion=informacion['descripcion'],
                                   entregado=informacion['entregado'])
                entrega.save()
                return HttpResponseRedirect(reverse('success'))
    else: 
        form= EntregaForm()
        return render(request, "entregaform.html", {"form":form})