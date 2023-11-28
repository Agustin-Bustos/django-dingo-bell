from django.shortcuts import render
from django.http import HttpResponse
import os
from flask import render_template, redirect
from .models import Libro
from .forms import LibroForm
from django.shortcuts import render, redirect
# Create your views here.
def inicio(request):
    #return HttpResponse("PRUEBA 1")
    return render(request, 'páginas/index.html')

def nosotros(request):
    return render(request, 'páginas/nosotros.html')

def libros(request):
    return render(request, 'libros/libros.html')

def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'libros/libros.html')

def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'libros/libros.html', {'libros':libros})

def crear(request):
    formulario = LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Libros')
    return render(request, 'libros/crear.html', {'formulario':formulario}
    )
    
def eliminar(request,id):
    libro= Libro.objects.get(id=id)
    libro.delete()
    return redirect('Libros')

def editar(request,id):
    libro=Libro.objects.get(id=id)
    #recuperamos la informacion del libro
    formulario = LibroForm(request.POST or None,request.FILES or None,instance=libro)
    if formulario.is_valid() and request.POST :
        formulario.save()
        return redirect('Libros')
    return render(request,'libros/editar.html',{'formulario':formulario})