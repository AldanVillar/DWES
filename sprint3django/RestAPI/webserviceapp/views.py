import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Tlibros
from .models import Tlibros, Tcomentarios

def pagina_de_prueba(request):
    return HttpResponse("<h1>Hola caracola</h1>")

def devolver_libros(request):

    lista_libros = Tlibros.objects.all()

    respuesta = []

    for libro in lista_libros:
        respuesta.append({
            "id": libro.id,
            "nombre": libro.nombre,
            "url_imagen": libro.url_imagen,
            "autor": libro.autor,
            "año": libro.año
        })

    return JsonResponse(respuesta, safe=False, json_dumps_params={'ensure_ascii': False})

def devolver_libro_por_id(request, id_solicitado):

    libro = Tlibros.objects.get(id=id_solicitado)

    comentarios = Tcomentarios.objects.filter(libro_id=id_solicitado)

    respuesta = {
        "id": libro.id,
        "nombre": libro.nombre,
        "url_imagen": libro.url_imagen,
        "autor": libro.autor,
        "año": libro.año,
        "comentarios": []
    }

    for comentario in comentarios:
        respuesta["comentarios"].append({
            "id": comentario.id,
            "comentario": comentario.comentario,
            "fecha": comentario.fecha,
            "usuario_id": comentario.usuario_id
        })

    return JsonResponse(respuesta, json_dumps_params={'ensure_ascii': False})

def insertar_comentario(request, id_solicitado):

    if request.method == "POST":

        datos = json.loads(request.body)
        texto = datos["nuevo_comentario"]

        # obtener libro
        libro = Tlibros.objects.get(id=id_solicitado)

        # crear nuevo comentario (usuario puede ser NULL)
        nuevo_comentario = Tcomentarios(
            comentario=texto,
            libro=libro
        )
        nuevo_comentario.save()

        return JsonResponse({})
