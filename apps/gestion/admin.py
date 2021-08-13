from django.contrib import admin
from apps.gestion.models import Modelo, Partida, Pregunta, Respuesta, Usuario

# Register your models here.

admin.site.register(Usuario)

admin.site.register(Pregunta)

admin.site.register(Partida)

admin.site.register(Modelo)

admin.site.register(Respuesta)