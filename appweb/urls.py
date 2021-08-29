from django.urls import path
from .views import (
    inicio,
    inicioUs,
    register,
)
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
)

urlpatterns = [
    path('', inicio.index, name= "index"),
    path('login/', LoginView.as_view(template_name= "login.html"), name= "login"),
    #path('logout/', LogoutView.as_view(template_name= "logout.html"), name= "logout"),
    path('inicio/logout/', LogoutView.as_view(template_name= "logout.html"), name= "logout"),
    path("register/", register, name="register"),
    path('inicio/', inicioUs.index, name= "inicioUs"),
]