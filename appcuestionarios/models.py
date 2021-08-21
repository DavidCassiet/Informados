from django.db import models
import random

# Create your models here.

CATEGORIAS_OPCION = (
    ('Cultura y arte', 'Cultura y arte'),
    ('Historia', 'Historia'),
    ('Deporte', 'Deporte'),
    ('Geografía', 'Geografía'), 
    ('Economía', 'Economía'), 
    ('Ciencia y Educación', 'Ciencia y Educación'), 
    ('Entretenimiento', 'Entretenimiento'), 
)

class Cuestionario(models.Model):
    nombre = models.CharField(max_length=120)
    categorias = models.CharField(max_length=19, choices=CATEGORIAS_OPCION)
    cant_preguntas = models.IntegerField()
    tiempo = models.IntegerField(help_text="duracion de partida")
    ptaje_requerido = models.IntegerField(help_text="puntaje requerido")
    
    def __str__(self):
        return f"{self.nombre}-{self.categorias}"

    def get_preguntas(self):
        preguntas = list(self.pregunta_set.all())
        random.shuffle(preguntas)
        return preguntas[:self.cant_preguntas]