from django.db import models
# Create your models here.
class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=100,verbose_name="Título")
    imagen= models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion= models.TextField(null=True, verbose_name="Descripcion")
    
    def __str__(self):
        fila= "Titulo: " + self.titulo + "-" + "Descripcion " 
        self.descripcion
        return fila
    def delete(self, using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete() 
        
        
class Comentarios(models.Model):
    ID_c=models.AutoField(primary_key=True)
    ID=models.ForeignKey(Libro, on_delete=models.CASCADE)
    Comentario=models.TextField(null=True,verbose_name="Comentario")
    
    def __str__(self):
        fila= "ID_c-ID: " + self.ID_c + "-" + self.ID +"Comentario" + self.Comentario
        return fila        
    
    
    