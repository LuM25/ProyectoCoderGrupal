from django.urls import path
from .views import *

app_name = 'recetas'

urlpatterns = [ 
    path('', ListaRecetas_1a3.as_view(), name = 'lista_recetas'),
    path('crear-receta/', CrearReceta_1a3.as_view(), name='crear_receta'),
]

