from django.db import models

class rutinas(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    objetivo = models.CharField(max_length=100)
    activo = models.BooleanField()
    # Asegúrate de que estos nombres coincidan EXACTAMENTE con tu BD
    fecha_modificacion = models.DateTimeField(db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(db_column='Fecha_creacion')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = '"rutinas"."rutinas"'
        managed = False

class grupos_musculares(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(db_column='descripcion')
    activo = models.BooleanField()
    fecha_modificacion = models.DateTimeField(db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(db_column='Fecha_creacion')
    
    class Meta:
        managed = False
        db_table = '"rutinas"."grupos_musculares"'
        
class ejercicios(models.Model):
    id = models.IntegerField(primary_key=True)
    grupo_muscular = models.ForeignKey(grupos_musculares, on_delete=models.DO_NOTHING, db_column='grupo_muscular_id')
    nombre = models.CharField(max_length=150)
    descripcion_corta = models.CharField(max_length=255)
    descripcion_larga = models.TextField()
    posicion_inicial = models.TextField()
    ejecucion = models.TextField()
    consejos = models.TextField()
    nivel = models.CharField(max_length=20)
    activo = models.BooleanField()
    fecha_modificacion = models.DateTimeField(db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(db_column='Fecha_creacion')

    class Meta:
        managed = False
        db_table = '"rutinas"."ejercicios"'