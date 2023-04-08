from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Vendedor, Comprador, Vehiculo
from django.shortcuts import render, redirect
from inicio.forms import CreacionCompradorFormulario, CreacionVendedorFormulario, CreacionVehiculoFormulario, BuscarAuto



def mi_vista(request):
    return render(request, 'inicio/index.html')

def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    template = loader.get_template(r'inicio/mostrar_fecha.html')
    
    datos = {'fecha': dt_formateado}
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)

def registrar_comprador(request):
    
    if request.method == "POST":
        formulario = CreacionCompradorFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            comprador = Comprador(nombre=datos_correctos['nombre'], apellido=datos_correctos['apellido'])
            comprador.save()

            return redirect('inicio:registrar_comprador')
    
    formulario = CreacionCompradorFormulario()
    return render(request, 'inicio/registrar_comprador.html', {'formulario': formulario})

def registrar_vendedor(request):
    
    if request.method == "POST":
        formulario = CreacionVendedorFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            vendedor = Vendedor(nombre=datos_correctos['nombre'], apellido=datos_correctos['apellido'], meses_de_contrato=datos_correctos["meses_de_contrato"])
            vendedor.save()

            return redirect('inicio:registrar_vendedor')
    
    formulario = CreacionVendedorFormulario()
    return render(request, 'inicio/registrar_vendedor.html', {'formulario': formulario})

# def lista_animales(request):
#     nombre_a_buscar = request.GET.get('nombre', None)
    
#     if nombre_a_buscar:
#         animales = Animal.objects.filter(nombre__icontains=nombre_a_buscar)
#     else:
#         animales = Animal.objects.all()
#     formulario_busqueda = BuscarAnimal()
#     return render(request, 'inicio/lista_animales.html', {'animales': animales, 'formulario': formulario_busqueda})

# def prueba_render(request):
#     datos = {'nombre': 'Pepe'}
#     return render(request, r'inicio/prueba_render.html', datos)
    