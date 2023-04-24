from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import RegistroPonto
from funcionario.models import CustomUser
from .forms import RegistroPontoForm

# Create your views here.


def ponto(request):
    # username = None

    if request.method == 'POST':
        form = RegistroPontoForm(request.POST)
        if form.is_valid() and request.POST.get('action') == 'create':
            registro = form.save(commit=False)
            registro.funcionario = request.user
            # registra o tipo oposto ao último.
            if (RegistroPonto.objects.filter(funcionario=request.user).exists()):
                registro.tipo = 'Saída' if (RegistroPonto.objects.filter(funcionario=request.user).latest('data_hora').tipo == 'Entrada') else 'Entrada'
            else:
                registro.tipo = 'Entrada'
            registro.save()
            return redirect('ponto')
        else:
            form = RegistroPontoForm()
            
            
    if request.user.is_authenticated:
        registros = RegistroPonto.objects.filter(funcionario=request.user)
        deltaSegundos = 0
        entradas = []

        for registro in registros:
            if registro.tipo == 'Entrada':
                entradas.append(registro.data_hora)
            else:
                if entradas:
                    # calcula a diferença entre a última Entrada e essa saída
                    delta = registro.data_hora - entradas[-1]
                    deltaSegundos += (delta.total_seconds())  # converte para horas
                    
        horario_provavel_fim_turno = registros[0].data_hora + timedelta(seconds=deltaSegundos) + timedelta(hours=8) if entradas else ""
        
        context = {'registros': registros, 'horario_provavel_fim_turno': horario_provavel_fim_turno,}

        return render(request, 'ponto.html', context)
