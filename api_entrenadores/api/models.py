from django.db import models


# Enum equivalente para estado
ESTADO_ENTRENADOR_CHOICES = [
    ('pendiente', 'Pendiente'),
    ('aprobado', 'Aprobado'),
    ('rechazado', 'Rechazado'),
    ('suspendido', 'Suspendido'),
]


# Tabla: entrenadores.entrenadores
class Entrenador(models.Model):
    id_entrenadores = models.AutoField(primary_key=True)
    id_adminitrador = models.IntegerField(null=True, blank=True)
    cedula = models.CharField(max_length=20, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    especialidad = models.CharField(max_length=150, null=True, blank=True)
    gimnasio_id = models.IntegerField(null=True, blank=True)
    anios_experiencia = models.IntegerField(null=True, blank=True)
    foto_url = models.CharField(max_length=255, null=True, blank=True)
    aprovacion_entrenador = models.BooleanField(default=False)
    hoja_vida = models.CharField(max_length=255, null=True, blank=True)
    calificacion_prom = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrenador {self.id_entrenadores} - {self.especialidad}"

    class Meta:
        db_table = 'entrenadores'


# Tabla: entrenadores.entrenador_documentos
class EntrenadorDocumento(models.Model):
    entrenador = models.ForeignKey(
        Entrenador,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column='entrenador_id'
    )
    identificacion = models.CharField(max_length=80, null=True, blank=True)
    nombre_archivo = models.CharField(max_length=150, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Documento {self.id} - {self.nombre_archivo}"

    class Meta:
        db_table = 'entrenador_documentos'


# Tabla: entrenadores.solicitudes_entrenador
class SolicitudEntrenador(models.Model):
    usuario_id = models.IntegerField(null=True, blank=True)
    gimnasio_id = models.IntegerField(null=True, blank=True)
    nombres_apellidos = models.CharField(max_length=200, null=True, blank=True)
    cedula = models.CharField(max_length=20, null=True, blank=True)
    experiencia = models.TextField(null=True, blank=True)
    sobre_mi = models.TextField(null=True, blank=True)
    especialidad = models.CharField(max_length=150, null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    correo = models.CharField(max_length=150, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_ENTRENADOR_CHOICES,
        default='pendiente'
    )
    revisado_por = models.BooleanField(default=False)
    revisado_en = models.DateTimeField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud {self.id} - {self.nombres_apellidos}"

    class Meta:
        db_table = 'solicitudes_entrenador'
