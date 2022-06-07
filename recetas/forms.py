from turtle import width
from django import forms
from .models import receta_1a3, receta_4a6, receta_7a10

class FormCrearReceta_1a3(forms.ModelForm):
    class Meta:
        model = receta_1a3
        fields = '__all__'

class FormCrearReceta_4a6(forms.ModelForm):
    class Meta:
        model = receta_4a6
        fields = '__all__'

class FormCrearReceta_7a10(forms.ModelForm):
    class Meta:
        model = receta_7a10
        fields = '__all__'