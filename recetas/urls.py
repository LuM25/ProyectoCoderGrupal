from django.urls import path
from .views import *

app_name = 'recetas'

urlpatterns = [ 
    path('', ListaRecetas_1a3.as_view(), name = 'lista_recetas'),
    path('crear-receta/', CrearReceta_1a3.as_view(), name='crear_receta'),
    path('crear-receta/', CrearReceta_4a6.as_view(), name='crear_receta'),
    path('crear-receta/', CrearReceta_7a10.as_view(), name='crear_receta'),
    path('buscar_receta/', buscar_receta, name= 'buscar_receta')
]

