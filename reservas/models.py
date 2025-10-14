from django.db import models  # Importa o sistema de modelos do Django
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão

# Modelo para Laboratório de informática
class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)  # Nome do laboratório
    capacidade = models.IntegerField()       # Capacidade máxima

    def __str__(self):
        return self.nome  # Exibe o nome no admin e consultas

# Modelo para Reserva de laboratório
class Reserva(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)  # Laboratório reservado
    professor = models.ForeignKey(User, on_delete=models.CASCADE)           # Usuário que fez a reserva
    data = models.DateField()                                               # Data da reserva
    horario_inicio = models.TimeField()                                     # Horário inicial
    horario_fim = models.TimeField()                                        # Horário final

    def __str__(self):
        # Exibe laboratório, data e usuário nas consultas/admin
        return f"{self.laboratorio.nome} - {self.data} ({self.professor.username})"