from django.db import models
from appcuestionarios.models import Cuestionario
from appweb.models import Usuario

# Create your models here.

class Resultado(models.Model):
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntaje = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.pk)