from django.db import models
from django.contrib.auth.models import User

# --------------------
# PERFIL (1:1)
# --------------------
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255)
    fecha_alta = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username


# --------------------
# AUTOR (1:N)
# --------------------
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# --------------------
# LIBRO (1:N)
# --------------------
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="libros")
    isbn = models.CharField(max_length=13, unique=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


# --------------------
# PRESTAMO
# --------------------
class Prestamo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    devuelto = models.BooleanField(default=False)

    # N:M con atributos extra
    libros = models.ManyToManyField(Libro, through='DetallePrestamo')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Préstamo #{self.id} - {self.usuario.username}"


# --------------------
# MODELO INTERMEDIO (N:M)
# --------------------
class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_devolucion = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['prestamo', 'libro'],
                name='unique_libro_por_prestamo'
            )
        ]

    def __str__(self):
        return f"{self.libro} x{self.cantidad}"
