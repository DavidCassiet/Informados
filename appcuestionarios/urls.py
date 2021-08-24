from django.urls import path
from .views import (
    CuestionarioListView,
    cuestionario_view,
    cuestionario_data_view,
    guardar_cuestionario_view,
)

app_name = 'appweb'

urlpatterns = [
    path('juego/', CuestionarioListView.as_view(), name='main-view'),
    path('juego/<pk>/', cuestionario_view, name= "cuestionario-view"),
    path('juego/<pk>/save/', guardar_cuestionario_view, name= "save-view"),
    path('juego/<pk>/data/', cuestionario_data_view, name= "cuestionario-data-view"),
    
]