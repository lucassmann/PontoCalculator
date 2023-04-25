from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum
from ponto.models import RegistroPonto
from funcionario.models import CustomUser
from .forms import UserDateForm
from django.contrib import messages
from datetime import timedelta, datetime
from django.contrib.admin.views.decorators import staff_member_required
import math
from decimal import Decimal


@staff_member_required
def dashboard(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        date_start = datetime.strptime(request.POST.get('date_start'), "%Y-%m-%d")
        date_end = datetime.strptime(request.POST.get('date_end'), "%Y-%m-%d")
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            messages.error(request, 'Usuário não encontrado')
            return redirect('dashboard')
        
        registros = RegistroPonto.objects.filter(funcionario=user, data_hora__date__range=[date_start, date_end])
        horas_extras = calcular_horas_extras(registros)      
        
        context = {
            'user': user,
            'registros': registros,
            'horas_extras': horas_extras,
            'date_start': date_start.strftime("%d/%m/%Y"),
            'date_end': date_end.strftime("%d/%m/%Y")
        }
        
        return render(request, 'resultado.html', context)
    
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    
    return render(request, 'selecionar_usuario.html', context)
    
    
def calcular_horas_extras(registros):
    
    horas_contratuais = 8
    total_horas = 0
    ultimo_registro = None
    
    for registro in registros:
        if registro.tipo == 'Entrada' or registro.tipo == 'Exceção(entrada)':
            ultimo_registro = registro
        elif registro.tipo == 'Saída' or registro.tipo == 'Exceção(saída)':
            if ultimo_registro is None:
                continue
            horas_trabalhadas = registro.data_hora - ultimo_registro.data_hora
            total_horas += horas_trabalhadas.total_seconds() / 3600
            ultimo_registro = None

    horas_extras = total_horas - horas_contratuais
    horas_extras = Decimal(horas_extras).quantize(Decimal('0.1'))
    return horas_extras if horas_extras > 0 else 0