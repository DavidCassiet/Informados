from appresultados.models import Resultado
from django.shortcuts import render

# Create your views here.

def ranking_general(request):
    ranking = Resultado.objects.all().order_by('-puntaje', 'cuestionario')
    return render(request, "ranking.html", {"resultados" : ranking})