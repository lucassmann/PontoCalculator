
from django.db import models
from funcionario.models import CustomUser
from django.utils import timezone

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=timezone.now, null=False)
    tipo = models.CharField(max_length=10, choices=(('entrada', 'Entrada'), ('saída', 'Saída'), ('excessao', 'excessão' 'Excessão')))
    detalhes = models.CharField(max_length=100, blank=True, null=True)