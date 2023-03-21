from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Usuarios

def index(request):
    return HttpResponse("Re-Re-Reiniciando la app")

def detail(request, usuarios_id):
    try:
        usuarios= Usuarios.objects.get(pk=usuarios_id)
    except Usuarios.DoesNotExist:
        raise Http404("El Usuario no existe")
    return render(request, 'remesas/detail.html',{'usuarios':usuarios})

# Create your views here.
def clientes(request):
    usuarios= Usuarios.objects.all().values()
    template=loader.get_template('all_clientes.html')
    context={
      'usuarios': usuarios,
    }
    return HttpResponse(template.render(context, request))

def ordenes(request):
    ordenes= Ordenes.objects.all().values()
    template= loader.get_template('all_clientes.html')
    context={
        'usuarios': usuarios, 
        }
    return HttpResponse(template.render(context,request))