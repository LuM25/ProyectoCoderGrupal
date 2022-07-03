from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from recetas.models import Receta
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from recetas.forms import FormCrearReceta
from django.contrib.auth.mixins import LoginRequiredMixin

########################################################## CREATE VIEW ########################################################################

class CrearReceta(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = FormCrearReceta 
    template_name = 'crear_receta.html'
    success_url = reverse_lazy('recetas:lista_recetas')
    login_url = reverse_lazy('users_app:user_login')


########################################################### LIST VIEW ########################################################################

class ListaRecetas(LoginRequiredMixin, ListView):
    model = Receta
    template_name= 'recetas.html'
    login_url = reverse_lazy('users_app:user_login')
    
    def get_context_data(self):
        context = {}
        lista_recetas = Receta.objects.all()
        context['lista_recetas'] = lista_recetas
        return context


########################################################### DETAIL VIEW ######################################################################

class DetailReceta(LoginRequiredMixin, DetailView):
    model = Receta
    template_name = 'detail_receta.html'
    login_url = reverse_lazy('users_app:user_login')

########################################################### DELETE VIEW ######################################################################

class EliminarReceta(LoginRequiredMixin, DeleteView):
    model = Receta
    template_name = 'eliminar_receta.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_success_url(self):
        return reverse('recetas:lista_recetas')

########################################################### UPDATE VIEW ######################################################################


class ActualizarReceta(LoginRequiredMixin, UpdateView):
    model = Receta
    template_name = 'actualizar_receta.html'
    fields = '__all__'
    login_url = reverse_lazy('users_app:user_login')

    def get_success_url(self):
        return reverse('recetas:detail_receta', kwargs = {'pk':self.object.pk})


########################################################### FUNCION BUSCAR ######################################################################


def buscar_receta(request):
    recetas = Receta.objects.filter(nombre__icontains=request.GET['search'])
    if recetas.exists():
        context = {'recetas':recetas}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'buscar_receta_1a3.html', context = context)

