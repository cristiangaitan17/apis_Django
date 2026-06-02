from django.db import models

# Create your models here.
from django.db import models

# ============================================
# SEDES GIMNASIOS
# ============================================
class SedeGimnasio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=30, unique=True, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    agregar_img = models.CharField(max_length=255, blank=True, null=True)
    agregar_sede = models.CharField(max_length=255, blank=True, null=True)
    aprovacion_entrenadores = models.BooleanField(default=False)
    calificacion_prom = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    total_resenas = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    administrador_id = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sedes_gimnasios'
        verbose_name = 'Sede Gimnasio'
        verbose_name_plural = 'Sedes Gimnasios'

    def __str__(self):
        return self.nombre


# ============================================
# GIMNASIO CLASES
# ============================================
class GimnasioClase(models.Model):
    id = models.AutoField(primary_key=True)
    gimnasio = models.ForeignKey(SedeGimnasio, on_delete=models.CASCADE, db_column='gimnasio_id', related_name='clases')
    nombre_clase = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'gimnasio_clases'
        verbose_name = 'Gimnasio Clase'
        verbose_name_plural = 'Gimnasio Clases'

    def __str__(self):
        return self.nombre_clase


# ============================================
# RESEÑAS GIMNASIO
# ============================================
class ResenaGimnasio(models.Model):
    id = models.AutoField(primary_key=True)
    gimnasio = models.ForeignKey(SedeGimnasio, on_delete=models.CASCADE, db_column='gimnasio_id', related_name='resenas')
    usuario_id = models.IntegerField()
    calificacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'resenas_gimnasio'
        verbose_name = 'Reseña Gimnasio'
        verbose_name_plural = 'Reseñas Gimnasio'

    def __str__(self):
        return f'Reseña de {self.gimnasio.nombre} - {self.calificacion} estrellas'