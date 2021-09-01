from django.contrib import admin
from .models import Resultado
# Register your models here.

class ResultadoAdmin(admin.ModelAdmin):
    list_display = ["usuario", "puntaje", "cuestionario"]

admin.site.register(Resultado, ResultadoAdmin)