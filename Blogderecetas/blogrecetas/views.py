from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class Index(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy('users_app:user_login')

class Contacto(LoginRequiredMixin, TemplateView):
    template_name = "contacto.html"
    login_url = reverse_lazy('users_app:user_login')


#def index(request):
    #return render(request, 'index.html')

#def contacto(request):
    #return render(request, 'contacto.html')