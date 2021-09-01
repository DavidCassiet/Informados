from django.shortcuts import render
from apppreguntas.models import Pregunta, Respuesta
from appresultados.models import Resultado
from django.http.response import JsonResponse
from .models import Cuestionario, Categoria
from django.views.generic import ListView

# Create your views here.

class CuestionarioListView(ListView):
    model = Cuestionario
    template_name = 'cuestionarios/main.html'

def cuestionario_view(request, pk):
    cuestonario = Cuestionario.objects.get(pk=pk)
    return  render(request, 'cuestionarios/cuestionario.html', {'obj': cuestonario})

def cuestionario_data_view(request, pk):
    cuestonario = Cuestionario.objects.get(pk=pk)
    preguntas = []
    for p in cuestonario.get_preguntas():
        respuestas = []
        for r in p.get_respuestas():
            respuestas.append(r.descripcion)
        preguntas.append({str(p): respuestas})
    return JsonResponse({
        'data': preguntas,
        'tiempo': cuestonario.tiempo,
    })

def guardar_cuestionario_view(request, pk):
    if request.is_ajax():
        preguntas = []
        data = request.POST
        data_ = dict(data.lists())
    
        data_.pop('csrfmiddlewaretoken')
    
        for k in data_.keys():
            print('key:', k)
            pregunta = Pregunta.objects.get(descripcion=k)
            preguntas.append(pregunta)
        print(preguntas)

        usuario = request.user
        cuestionario = Cuestionario.objects.get(pk=pk)

        puntaje = 0
        multiplicador = 100 / cuestionario.cant_preguntas
        resultados = []
        respuesta_correcta = None

        for p in preguntas:
            r_seleccionada = request.POST.get(p.descripcion)
            
            if r_seleccionada != "":
                pregunta_respuestas = Respuesta.objects.filter(pregunta=p)
                for r in pregunta_respuestas:
                    if r_seleccionada == r.descripcion:
                        if r.validacion:
                            puntaje += 1
                            respuesta_correcta = r.descripcion
                    else:
                        if r.validacion:
                            respuesta_correcta = r.descripcion
                    
                resultados.append({str(p): {'respuesta_correcta': respuesta_correcta, 'respondida': r_seleccionada}})
            else:
                resultados.append({str(p): 'no respondida'})
        puntaje_ = puntaje * multiplicador
        Resultado.objects.create(cuestionario=cuestionario, usuario=usuario, puntaje=puntaje_)

        if puntaje_ >= cuestionario.ptaje_requerido:
            return JsonResponse({'pasado': True, 'puntaje': puntaje_, 'resultados': resultados})
        else:
            return JsonResponse({'pasado': False, 'puntaje': puntaje_, 'resultados': resultados})
