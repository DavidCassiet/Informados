from enum import unique
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import Field, NullBooleanField
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    contraseña = models.CharField(max_length=50, null=False, blank=False)
    #creada_en=models.DateTimeField(auto_now_add=True)

class Pregunta(models.Model):
    descripcion = models.TextField()
    FechaCrea = models.DateField(auto_now_add=True)

class Partida(models.Model):
    nivel = models.IntegerField()
    fechaIni = models.DateField(auto_now_add=True)
    progreso = models.FloatField()
    puntos = models.IntegerField()
    part_preg= models.ManyToManyField(Pregunta,through="Modelo",blank=True)

    class Meta:
        db_table = "Partidas"
        ordering = ["-fechaIni"]

class Modelo(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE,
    blank=True,null=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE,
    blank=True,null=True)
    acierta = models.BooleanField()

class Respuesta(models.Model):
    validacion = models.BooleanField()
    descripcion = models.TextField()
    IdPreg = models.ForeignKey(Pregunta, on_delete=models.CASCADE ,null=True, blank=True)

#Esta clase sale de la relacion pregunta - partida (n,n)

#class Muestra_part_preg(models.Model):
#    IdPartida= models.ForeignKey(Partida, on_delete=models.CASCADE ,null=True, blank=True)
#    IdPreg = models.ForeignKey(Pregunta, on_delete=models.CASCADE ,null=True, blank=True)
#    acierta = models.BooleanField()