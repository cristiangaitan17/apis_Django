import os
import django
from django.conf import settings

# Configurar el entorno de Django manualmente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.db import connection

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        row = cursor.fetchone()
        print("¡Éxito! Conectado a:", row[0])
except Exception as e:
    print("Error de conexión:", e)