from django.contrib import admin
from appweb.models import Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class PerfilAdmin(UserAdmin):
    list_display = ['username', 'is_staff', 'is_active']

admin.site.register(Usuario, PerfilAdmin)