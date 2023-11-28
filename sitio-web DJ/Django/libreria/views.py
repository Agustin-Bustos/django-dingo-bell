from django.shortcuts import render
from django.http import HttpResponse
import os
from flask import render_template, redirect
from .models import Comentarios, Libro
from .forms import LibroForm, comentariosForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def comentar(request,id):
    formulario = comentariosForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('/libros')
    return render(request, 'libros/comentar.html', {'coment':id})


def com(request,id):
    comentarios = Comentarios.objects.filter(ID=id)
    return render(request, 'libros/com.html', {'comentarios':comentarios})

def eliminarc(request,id):
    comentario= Comentarios.objects.get(ID_c=id)
    comentario.delete()
    return redirect('com')

def editarc(request,id):
    comentarios=Comentarios.objects.get(ID_c=id)
    formulario = comentariosForm(request.POST or None,request.FILES or None, instance=Comentarios)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editarcom.html',{'formulario':formulario})