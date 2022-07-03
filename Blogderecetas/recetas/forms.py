from turtle import width
from django import forms
from .models import Receta
class FormCrearReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'