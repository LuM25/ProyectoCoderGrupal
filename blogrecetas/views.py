from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')