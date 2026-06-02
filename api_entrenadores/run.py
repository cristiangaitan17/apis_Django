import os
from decouple import config

#leer el puerto .env
port = config('API_PORT')

#ejecutar el servidor de desarrollo de Django en el puerto especificado

# Apunta a la subcarpeta antes de llamar a manage.py gggg
os.system(f'python gymfit_login_api/manage.py runserver {port}')