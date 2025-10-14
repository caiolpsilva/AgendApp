from django.contrib import admin  # Importa o módulo de administração do Django
from .models import Laboratorio, Reserva  # Importa os modelos Laboratorio e Reserva do arquivo models.py


# Registra o modelo Laboratorio no painel administrativo do Django
admin.site.register(Laboratorio)

# Registra o modelo Reserva no painel administrativo do Django
admin.site.register(Reserva)
