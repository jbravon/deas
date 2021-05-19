from django.shortcuts import render
from django.http import HttpResponse
from numpy import result_type
from .queries import *
from .models import DEA

# Create your views here.

def index(request):
    deas = DEA.objects.all()
    dea, url = nearest_dea(40.4600052, -3.6285832, deas)
    context = {"dea": dea, "url": url}
    return render(request, "finder/index.html", context)


def listado(request):
    # insert_into(data) #Importacion de la BD
    # return HttpResponse("Se encuentra en la página Index")
    deas = DEA.objects.all()
    context = {"deas": deas}
    return render(request, "finder/listado.html", context)


def contact(request):
    return HttpResponse("Se encuentra en la página de contactos")