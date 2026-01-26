from rest_framework import serializers
from .models import Libro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    autor_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Libro
        fields = [
            'id',
            'titulo',
            'isbn',
            'precio',
            'stock',
            'disponible',
            'autor',
            'autor_id'
        ]
        extra_kwargs = {
            'id': {'read_only': True}
        }
