from django.urls import path
from recetas.views import recetas

urlpatterns = [ 
    path('recetas/', recetas, name = recetas),
]
