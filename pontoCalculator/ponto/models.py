
from django.db import models
from funcionario.models import CustomUser
from django.utils import timezone

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=timezone.now, null=False)
    tipo = models.CharField(max_length=20, choices=(('Entrada', 'entrada', ), ('Saída', 'saída'), ('Exceção(entrada)', 'exceçao(entrada)'), ('Exceção(saída)', 'exceçao(saída)'), ('Férias', 'férias')))
    detalhes = models.CharField(max_length=100, blank=True, null=True)