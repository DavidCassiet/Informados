from django.db import models
import random

# Create your models here.

class Categoria(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nombre

class Cuestionario(models.Model):
    nombre = models.CharField(max_length=120)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cant_preguntas = models.IntegerField()
    tiempo = models.IntegerField(help_text="duracion de partida en minutos")
    ptaje_requerido = models.IntegerField(help_text="puntaje requerido en % (- de 100%)")
    
    def __str__(self):
        return f"{self.nombre}-{self.categorias}"

    def get_preguntas(self):
        preguntas = list(self.pregunta_set.all())
        random.shuffle(preguntas)
        return preguntas[:self.cant_preguntas]