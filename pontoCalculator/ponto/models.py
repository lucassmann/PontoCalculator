
from django.db import models
from funcionario.models import CustomUser

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=(('entrada', 'Entrada'), ('saída', 'Saída')))
    detalhes = models.CharField(max_length=100, blank=True, null=True)