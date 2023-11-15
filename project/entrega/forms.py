from django import forms
from .models import Entrega
class EntregaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=200)
    entregado = forms.BooleanField(required=True)
    class Meta:
        model = Entrega
        fields = "__all__"