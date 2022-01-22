from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='proyectos')

    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'

    def __str__(self):
        return self.titulo