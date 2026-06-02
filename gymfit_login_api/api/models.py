from django.db import models


ROL_CHOICES = [
    ('admin', 'Admin'),
    ('usuario', 'Usuario'),
    ('entrenador', 'Entrenador'),
]


# Tabla: login.administrador
class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    nombre_gym = models.CharField(max_length=150, null=True, blank=True)
    nit = models.CharField(max_length=30, null=True, blank=True)
    anio_fundacion = models.IntegerField(null=True, blank=True)
    cantidad_clientes = models.IntegerField(null=True, blank=True)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    propietario_nombre = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.CharField(max_length=150, null=True, blank=True)
    pagina_web = models.CharField(max_length=255, null=True, blank=True)
    firma = models.CharField(max_length=255, null=True, blank=True)
    fecha_firma = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_gym or f"Administrador {self.id_administrador}"

    class Meta:
        db_table = 'administrador'


# Tabla: login.usuarios
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=80, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        db_table = 'usuarios'


# Tabla: login.login
class Login(models.Model):
    id_login = models.AutoField(primary_key=True)
    id_nombre = models.IntegerField(null=True, blank=True)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Login {self.id_login} - rol: {self.rol}"

    class Meta:
        db_table = 'login'
