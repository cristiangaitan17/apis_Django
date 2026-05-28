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