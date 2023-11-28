from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('nosotros/', views.nosotros, name='Nosotros'),
    path('libros/', views.libros, name='Libros'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar , name='editar'),
    path('libros/crear/',views.crear, name='crear')
]