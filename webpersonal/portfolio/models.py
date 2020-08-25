from django.db import models

# Create your models here.

class Project(models.Model):
    titulo = models.CharField(max_length=200, verbose_name= "Titulo")
    description= models.TextField(verbose_name= "Descripcion")
    image=models.ImageField( verbose_name = "Imagen", upload_to= "projects")
    created= models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    update= models.DateTimeField(auto_now=True, verbose_name= "Fecha de edicion")
    url= models.URLField(null=True , blank= True , verbose_name= "Mas Informacion")

    class Meta:
       verbose_name = 'proyecto'
       verbose_name_plural = 'proyectos'
       ordering = ["-created"]
    def __str__(self):
        return self.titulo
