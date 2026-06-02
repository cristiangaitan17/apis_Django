from django.db import models

# Create your models here.
from django.db import models

# ============================================
# CATEGORÍAS
# ============================================
class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    seccion_lugar = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


# ============================================
# NOTICIAS
# ============================================
class Noticia(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='noticias')
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(blank=True, null=True)
    encabezado = models.CharField(max_length=255, blank=True, null=True)
    imagen_principal = models.CharField(max_length=255, blank=True, null=True)
    autor_id = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='borrador')
    vistas = models.IntegerField(default=0)
    publicado_en = models.DateTimeField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Noticias'
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo


# ============================================
# ARTÍCULOS SECCIONES
# ============================================
class ArticuloSeccion(models.Model):
    articulo = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='secciones')
    titulo_seccion = models.CharField(max_length=200, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    imagen_url = models.CharField(max_length=255, blank=True, null=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articulos_secciones'
        verbose_name = 'Artículo Sección'
        verbose_name_plural = 'Artículos Secciones'

    def __str__(self):
        return self.titulo_seccion or f'Sección {self.id}'


# ============================================
# NUTRICIÓN
# ============================================
class Nutricion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    imagen_url = models.CharField(max_length=255, blank=True, null=True)
    autor_id = models.IntegerField(blank=True, null=True)
    publicado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Nutricion'
        verbose_name = 'Nutrición'
        verbose_name_plural = 'Nutriciones'

    def __str__(self):
        return self.nombre


# ============================================
# DIETA COMIDAS
# ============================================
class DietaComida(models.Model):
    dieta = models.ForeignKey(Nutricion, on_delete=models.CASCADE, related_name='comidas')
    tiempo_comida = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dieta_comidas'
        verbose_name = 'Dieta Comida'
        verbose_name_plural = 'Dieta Comidas'

    def __str__(self):
        return f'{self.tiempo_comida} - {self.dieta.nombre}'


# ============================================
# COMENTARIOS COMUNIDAD
# ============================================
class ComentarioComunidad(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='comentarios')
    usuario_id = models.IntegerField()
    contenido = models.TextField()
    calificacion = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, default='activo')
    activo = models.BooleanField(default=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comentarios_comunidad'
        verbose_name = 'Comentario Comunidad'
        verbose_name_plural = 'Comentarios Comunidad'

    def __str__(self):
        return f'Comentario {self.id} - {self.contenido[:50]}'


# ============================================
# RESPUESTAS COMENTARIO
# ============================================
class RespuestaComentario(models.Model):
    comentario = models.ForeignKey(ComentarioComunidad, on_delete=models.CASCADE, related_name='respuestas')
    usuario_id = models.IntegerField()
    contenido = models.TextField()
    activo = models.BooleanField(default=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'respuestas_comentario'
        verbose_name = 'Respuesta Comentario'
        verbose_name_plural = 'Respuestas Comentario'

    def __str__(self):
        return f'Respuesta {self.id} - {self.contenido[:50]}'
    
    