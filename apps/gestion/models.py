from enum import unique
from django.db import models
from django.db.models.fields import Field, NullBooleanField

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    contraseña = models.CharField(max_length=50, null=False, blank=False)

class Partida(models.Model):
    nivel = models.IntegerField()
    fecha = models.DateField()
    
class Pregunta(models.Model):
    descripcion = models.TextField()

class Respuesta(models.Model):
    validacion = models.BooleanField()
    descripcion = models.TextField()
    pregunta = models.ForeignKey(Pregunta, null=True, blank=True)

#Esta clase sale de la relacion pregunta - respuesta (n,n)

class Pregunta_Respuesta(models.Model):
    validacion = models.BooleanField()
    id_preg = Field.primary_key=True(null=False, unique=True)
    id_resp = Field.primary_key=True(null=False, unique=True)
    pregunta = models.ForeignKey()