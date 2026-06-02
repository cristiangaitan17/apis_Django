
import os
from decouple import config

# LEER EL PUERTO DESDE EL ARCHIVO .ENV
port = config('API_PORT', default='8000')

# INICIAR EL SERVIDOR DE DESARROLLO DE DJANGO EN EL PUERTO LEIDO
os.system(f'python manage.py runserver {port}')