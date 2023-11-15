from django import forms
from .models import Estudiante
class EstudianteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()
    class Meta:
        model = Estudiante
        fields = "__all__"