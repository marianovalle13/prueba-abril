from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    context = {} 
    context['facturas']= Factura.objects.all()

    return render(request, "index.html", context)

def boton(request, nrofactura):
    context = {}
    context ['facturas_mas']=Factura.objects.filter(nrofactura=nrofactura)

    return render(request, "boton.html", context)


