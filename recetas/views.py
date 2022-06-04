from django.shortcuts import render

from recetas.models import receta_1a3
from recetas.models import receta_4a6
from recetas.models import receta_7a10

# Create your views here.

def recetas(request):
    receta1_3 = receta_1a3.objects.all
    receta4_6 = receta_4a6.objects.all
    receta7_10 = receta_7a10.objects.all
    context = {'receta1_3': receta1_3, 'receta4_6': receta4_6, 'receta7_10': receta7_10}
    return render(request,'recetas.html', context = context)
