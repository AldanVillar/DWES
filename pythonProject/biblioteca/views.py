from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Libro

class LibroListCreateAPIView(APIView):

    # GET /api/libros/
    def get(self, request):
        libros = Libro.objects.all()
        data = []

        for libro in libros:
            data.append({
                'id': libro.id,
                'titulo': libro.titulo,
                'isbn': libro.isbn,
                'precio': libro.precio,
                'stock': libro.stock,
                'disponible': libro.disponible
            })

        return Response(data, status=status.HTTP_200_OK)

    # POST /api/libros/
    def post(self, request):
        data = request.data

        libro = Libro.objects.create(
            titulo=data.get('titulo'),
            isbn=data.get('isbn'),
            precio=data.get('precio'),
            stock=data.get('stock'),
            disponible=data.get('disponible', True),
            autor_id=data.get('autor')  # se pasa el id del autor
        )

        return Response(
            {
                'id': libro.id,
                'mensaje': 'Libro creado correctamente'
            },
            status=status.HTTP_201_CREATED
        )


class LibroDetailAPIView(APIView):

    # GET /api/libros/{id}/
    def get(self, request, pk):
        try:
            libro = Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            return Response(
                {'error': 'Libro no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )

        data = {
            'id': libro.id,
            'titulo': libro.titulo,
            'isbn': libro.isbn,
            'precio': libro.precio,
            'stock': libro.stock,
            'disponible': libro.disponible
        }

        return Response(data, status=status.HTTP_200_OK)
