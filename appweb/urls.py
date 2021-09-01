from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
)

urlpatterns = [
    path('', views.inicio.index, name= "index"),
    path('login/', LoginView.as_view(template_name= "login.html"), name= "login"),
    #path('logout/', LogoutView.as_view(template_name= "logout.html"), name= "logout"),
    path('inicio/logout/', LogoutView.as_view(template_name= "logout.html"), name= "logout"),
    path("register/", views.register, name="register"),
    path('inicio/', views.inicioUs.index, name= "inicioUs"),
]