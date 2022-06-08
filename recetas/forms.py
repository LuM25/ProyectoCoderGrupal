from turtle import width
from django import forms
from .models import Receta_1a3, Receta_4a6, Receta_7a10

class FormCrearReceta_1a3(forms.ModelForm):
    class Meta:
        model = Receta_1a3
        fields = '__all__'

class FormCrearReceta_4a6(forms.ModelForm):
    class Meta:
        model = Receta_4a6
        fields = '__all__'

class FormCrearReceta_7a10(forms.ModelForm):
    class Meta:
        model = Receta_7a10
        fields = '__all__'