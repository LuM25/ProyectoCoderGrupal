from django.shortcuts import render
from django.http import HttpResponse
from recetas.models import Receta_1a3, Receta_4a6, Receta_7a10
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView
from recetas.forms import FormCrearReceta_1a3, FormCrearReceta_4a6, FormCrearReceta_7a10 

# Create your views here.

class CrearReceta_1a3(CreateView):
    model = Receta_1a3
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class ListaRecetas_1a3(ListView):
    model = Receta_1a3
    template_name= 'recetas.html'

class CrearReceta_4a6(CreateView):
    model = Receta_4a6
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class ListaRecetas_4a6(ListView):
    model = Receta_4a6
    template_name= 'recetas.html'

class CrearReceta_7a10(CreateView):
    model = Receta_7a10
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class ListaRecetas_7a10(ListView):
    model = Receta_7a10
    template_name= 'recetas.html'

def buscar_receta(request):
    receta1_a3 =  Receta_1a3.objects.filter(name__icontains=request.GET['search'])
    if receta1_a3.exists():
        context = {'receta_1a3': receta1_a3}
    else:
        context = {'errors':'No se encontro la receta'}
    return render(request, 'buscar_receta.html', context = context)