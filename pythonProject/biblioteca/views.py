from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Libro, Autor
from .serializers import LibroSerializer, AutorSerializer
from rest_framework.viewsets import ModelViewSet


class LibroListCreateAPIView(APIView):

    # GET lista
    def get(self, request):
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST crear
    def post(self, request):
        serializer = LibroSerializer(data=request.data)

        if serializer.is_valid():
            libro = serializer.save(autor_id=request.data.get('autor_id'))
            return Response(
                LibroSerializer(libro).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibroDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            libro = Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            return Response(
                {'error': 'Libro no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = LibroSerializer(libro)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

