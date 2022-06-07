from turtle import width
from django import forms
from .models import receta_1a3

class FormCrearReceta_1a3(forms.ModelForm):
    class Meta:
        model = receta_1a3
        fields = '__all__'