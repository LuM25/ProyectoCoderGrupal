from django.urls import path
from .views import *

app_name = 'recetas'

urlpatterns = [ 
    path('', ListaRecetas.as_view(), name = 'lista_recetas'),

    path('buscar-receta-1a3/', buscar_receta_1a3, name = 'buscar_receta_1a3'),
    path('buscar-receta-4a6/', buscar_receta_4a6, name = 'buscar_receta_4a6'),
    path('buscar-receta-7a10/', buscar_receta_7a10, name = 'buscar_receta_7a10'),

    path('crear-receta-1a3/', CrearReceta_1a3.as_view(), name='crear_receta_1a3'),
    path('crear-receta-4a6/', CrearReceta_4a6.as_view(), name='crear_receta_4a6'),
    path('crear-receta-7a10/', CrearReceta_7a10.as_view(), name='crear_receta_7a10'),
    
    path('detail-receta-1a3/<int:pk>/', DetailReceta_1a3.as_view(), name='detail_receta_1a3'),
    path('detail-receta-4a6/<int:pk>/', DetailReceta_4a6.as_view(), name='detail_receta_4a6'),
    path('detail-receta-7a10/<int:pk>/', DetailReceta_7a10.as_view(), name='detail_receta_7a10'),

    path('eliminar-receta-1a3/<int:pk>/', EliminarReceta_1a3.as_view(), name='eliminar_receta_1a3'),
    path('eliminar-receta-4a6/<int:pk>/', EliminarReceta_4a6.as_view(), name='eliminar_receta_4a6'),
    path('eliminar-receta-7a10/<int:pk>/', EliminarReceta_7a10.as_view(), name='eliminar_receta_7a10'),

    path('actualizar-receta-1a3/<int:pk>/', ActualizarReceta_1a3.as_view(), name='actualizar_receta_1a3'),
    path('actualizar-receta-4a6/<int:pk>/', ActualizarReceta_4a6.as_view(), name='actualizar_receta_4a6'),
    path('actualizar-receta-7a10/<int:pk>/', ActualizarReceta_7a10.as_view(), name='actualizar_receta_7a10'),


]

