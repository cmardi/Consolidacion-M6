from django import forms
from .models import VehiculoModel

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = VehiculoModel
        fields = "__all__"
        
        