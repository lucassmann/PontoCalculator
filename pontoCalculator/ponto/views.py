from django.shortcuts import render
from django.http import HttpResponse
from .models import RegistroPonto
# Create your views here.


def ponto(request):
    # username = None
    if request.user.is_authenticated:
        #     username = request.user.username
        # context = {'username': username}
        return render(request, 'ponto.html')

def registrar_ponto(request):
    registro = RegistroPonto()
    registro.save()
    return HttpResponse("Ponto registrado com sucesso!")