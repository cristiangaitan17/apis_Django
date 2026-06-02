from django.contrib import admin
from .models import Entrenador, EntrenadorDocumento, SolicitudEntrenador

admin.site.register(Entrenador)
admin.site.register(EntrenadorDocumento)
admin.site.register(SolicitudEntrenador)
