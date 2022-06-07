from django.shortcuts import render
from django.http import HttpResponse
from recetas.models import receta_1a3, receta_4a6, receta_7a10
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from .models import receta_1a3, receta_4a6, receta_7a10
from recetas.forms import FormCrearReceta_1a3

# Create your views here.

#def recetas(request):
#    receta1_3 = receta_1a3.objects.all
#    receta4_6 = receta_4a6.objects.all
#   receta7_10 = receta_7a10.objects.all
#    context = {'receta1_3': receta1_3, 'receta4_6': receta4_6, 'receta7_10': receta7_10}
#    return render(request,'recetas.html', context = context)

class CrearReceta_1a3(CreateView):
    model = receta_1a3
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class ListaRecetas_1a3(ListView):
    model = receta_1a3
    template_name= 'recetas.html'

