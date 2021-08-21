from django.db import models
from appcuestionarios.models import Cuestionario

# Create your models here.

class Pregunta(models.Model):
    descripcion = models.TextField()
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.descripcion)

    def get_respuestas(self):
        return self.respuesta_set.all()

class Respuesta(models.Model):
    descripcion = models.TextField()
    validacion = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE ,null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"pregunta: {self.pregunta.descripcion}, respuesta: {self.descripcion}, correcta: {self.validacion}"