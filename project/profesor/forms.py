from django import forms
from .models import Profesor
class ProfesorForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()
    class Meta:
        model = Profesor
        fields = "__all__"
        
class BuscarProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=30)