from django.urls import path
from . import views

urlpatterns = [
    path('juego/', views.CuestionarioListView.as_view(), name='main-view'),
    path('juego/<pk>/', views.cuestionario_view, name= "cuestionario-view"),
    path('juego/<pk>/save/', views.guardar_cuestionario_view, name= "save-view"),
    path('juego/<pk>/data/', views.cuestionario_data_view, name= "cuestionario-data-view"),
    
    path('categorias/', views.categorias, name= "categorias"),

]