from django.shortcuts import render
from django.http import HttpResponse
from recetas.models import receta_1a3, receta_4a6, receta_7a10
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView
from .models import receta_1a3, receta_4a6, receta_7a10
from recetas.forms import FormCrearReceta_1a3

# Create your views here.

class CrearReceta_1a3(CreateView):
    model = receta_1a3
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class ListaRecetas_1a3(ListView):
    model = receta_1a3
    template_name= 'recetas.html'

class CrearReceta_4a6(CreateView):
    model = receta_4a6
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class ListaRecetas_4a6(ListView):
    model = receta_4a6
    template_name= 'recetas.html'

class CrearReceta_7a10(CreateView):
    model = receta_7a10
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class ListaRecetas_7a10(ListView):
    model = receta_7a10
    template_name= 'recetas.html'

