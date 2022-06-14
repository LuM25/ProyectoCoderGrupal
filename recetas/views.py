from django.shortcuts import render
from django.http import HttpResponse
from recetas.models import Receta_1a3, Receta_4a6, Receta_7a10
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from recetas.forms import FormCrearReceta_1a3, FormCrearReceta_4a6, FormCrearReceta_7a10 

# Create your views here.

########################################################## CREATE VIEW ########################################################################

class CrearReceta_1a3(CreateView):
    model = Receta_1a3
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta_1a3.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class CrearReceta_4a6(CreateView):
    model = Receta_4a6
    form_class = FormCrearReceta_4a6
    template_name = 'crear_receta_4a6.html'
    success_url = reverse_lazy('recetas:lista_recetas')

class CrearReceta_7a10(CreateView):
    model = Receta_7a10
    form_class = FormCrearReceta_7a10
    template_name = 'crear_receta_7a10.html'
    success_url = reverse_lazy('recetas:lista_recetas')

########################################################### LIST VIEW ########################################################################

class ListaRecetas(ListView):
    model = Receta_1a3
    template_name= 'recetas.html'
    
    def get_context_data(self):
        context = {}
        lista_recetas_1a3 = Receta_1a3.objects.all()
        lista_recetas_4a6 = Receta_4a6.objects.all()
        lista_recetas_7a10 = Receta_7a10.objects.all()
        context['lista_recetas_1a3'] = lista_recetas_1a3
        context['lista_recetas_4a6'] = lista_recetas_4a6
        context['lista_recetas_7a10'] = lista_recetas_7a10
        return context


########################################################### DETAIL VIEW ######################################################################

class DetailReceta_1a3(DetailView):
    model = Receta_1a3
    template_name = 'detail_receta_1a3.html'

class DetailReceta_4a6(DetailView):
    model = Receta_4a6
    template_name = 'detail_receta_4a6.html'

class DetailReceta_7a10(DetailView):
    model = Receta_7a10
    template_name = 'detail_receta_7a10.html'

########################################################### DELETE VIEW ######################################################################

class EliminarReceta_1a3(DeleteView):
    model = Receta_1a3
    template_name = 'eliminar_receta_1a3.html'

    def get_success_url(self):
        return reverse('lista_recetas')

class EliminarReceta_4a6(DeleteView):
    model = Receta_4a6
    template_name = 'eliminar_receta_4a6.html'

    def get_success_url(self):
        return reverse('lista_recetas')

class EliminarReceta_7a10(DeleteView):
    model = Receta_7a10
    template_name = 'eliminar_receta_7a10.html'

    def get_success_url(self):
        return reverse('lista_recetas')

########################################################### UPDATE VIEW ######################################################################


class ActualizarReceta_1a3(UpdateView):
    model = Receta_1a3
    template_name = 'actualizar_receta_1a3.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('recetas:detail_receta_1a3', kwargs = {'pk':self.object.pk})

class ActualizarReceta_4a6(UpdateView):
    model = Receta_4a6
    template_name = 'actualizar_receta_4a6.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('recetas:detail_receta_4a6', kwargs = {'pk':self.object.pk})

class ActualizarReceta_7a10(UpdateView):
    model = Receta_7a10
    template_name = 'actualizar_receta_7a10.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('recetas:detail_receta_7a10', kwargs = {'pk':self.object.pk})

########################################################### SEARCH VIEW ######################################################################
def buscar_receta_1a3(request):
    recetas = Receta_1a3.objects.filter(name__icontains=request.GET['search'])
    if recetas.exists():
        context = {'recetas':recetas}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'buscar_receta_1a3.html', context = context)

def buscar_receta_4a6(request):
    recetas = Receta_4a6.objects.filter(name__icontains=request.GET['search'])
    if recetas.exists():
        context = {'recetas':recetas}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'buscar_receta_4a6.html', context = context)

def buscar_receta_7a10(request):
    recetas = Receta_7a10.objects.filter(name__icontains=request.GET['search'])
    if recetas.exists():
        context = {'recetas':recetas}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'buscar_receta_7a10.html', context = context)
