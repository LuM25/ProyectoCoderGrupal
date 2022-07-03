from django.urls import path
from .views import *

app_name = 'recetas'

urlpatterns = [
    path('buscar-receta/', buscar_receta, name = 'buscar_receta'),
    path('', ListaRecetas.as_view(), name = 'lista_recetas'),
    path('crear-receta/', CrearReceta.as_view(), name='crear_receta'),
    path('detail-receta/<int:pk>/', DetailReceta.as_view(), name='detail_receta'),
    path('eliminar-receta/<int:pk>/', EliminarReceta.as_view(), name='eliminar_receta'),
    path('actualizar-receta/<int:pk>/', ActualizarReceta.as_view(), name='actualizar_receta'),
]

