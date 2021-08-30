from django.contrib import admin
from .models import Categoria, Cuestionario

# Register your models here.

admin.site.register(Cuestionario)

admin.site.register(Categoria)