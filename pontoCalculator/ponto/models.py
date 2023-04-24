
from django.db import models
from funcionario.models import CustomUser

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)