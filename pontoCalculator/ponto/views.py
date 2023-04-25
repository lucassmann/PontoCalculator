from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from .models import RegistroPonto
from funcionario.models import CustomUser
from .forms import RegistroPontoForm, RegistroPontoAdmin
from django.http import HttpResponseForbidden

# Create your views here.


def ponto(request):
    # username = None

    if request.user.is_authenticated:
        now = timezone.now() # obter a data e hora atuais do timezone padrão
        start_of_day = timezone.make_aware(timezone.datetime(now.year, now.month, now.day, 0, 0, 0)) # obter a data e hora do início do dia atual
        end_of_day = timezone.make_aware(timezone.datetime(now.year, now.month, now.day, 23, 59, 59)) # obter a data e hora do final do dia atual
        if RegistroPonto.objects.filter(funcionario=request.user, data_hora__range=(start_of_day, end_of_day)).exists():
            registros_do_dia_atual = RegistroPonto.objects.filter(funcionario=request.user, data_hora__range=(start_of_day, end_of_day))
            ferias = RegistroPonto.objects.filter(funcionario=request.user, data_hora__range=(start_of_day, end_of_day), tipo='Férias')
        else:
            registros_do_dia_atual = None
            ferias = None
        if request.method == 'POST':
            form = RegistroPontoForm(request.POST)
            if form.is_valid() and request.POST.get('action') == 'create':
                if ferias:
                    return HttpResponseForbidden("Você está de férias, divirta-se em outro lugar!")
                registro = form.save(commit=False)
                registro.funcionario = request.user
                # registra o tipo oposto ao último.
                if (registros_do_dia_atual):
                    registro.tipo = 'Saída' if (RegistroPonto.objects.filter(funcionario=request.user, data_hora__range=(start_of_day, end_of_day)).latest('data_hora').tipo == 'Entrada') else 'Entrada'
                else:
                    registro.tipo = 'Entrada'
                registro.save()
                return redirect('ponto')
            else:
                form = RegistroPontoForm()
        if not registros_do_dia_atual:
            return render(request, 'ponto.html', {'registros': '', 'horario_provavel_fim_turno': ''})
        else: 
            saidas = []
            intervaloMinutos = 0
            
            for registro in registros_do_dia_atual:
                if 'saída' in registro.tipo.lower():
                    saidas.append(registro.data_hora)
                else:
                    if saidas and ('entrada' in registro.tipo.lower()):
                        delta = registro.data_hora - saidas[-1]
                        intervaloMinutos += (delta.total_seconds() /60)
                    else:
                        intervaloMinutos = 0
            
            horario_provavel_fim_turno = registros_do_dia_atual[0].data_hora + timedelta(hours=8) + timedelta(minutes=intervaloMinutos)
            context = {'registros': registros_do_dia_atual, 'horario_provavel_fim_turno': horario_provavel_fim_turno,}
            return render(request, 'ponto.html', context)

def admin(request):
    
    if request.user.is_authenticated:
        now = timezone.now() # obter a data e hora atuais do timezone padrão
        start_of_day = timezone.make_aware(timezone.datetime(now.year, now.month, now.day, 0, 0, 0)) # obter a data e hora do início do dia atual
        end_of_day = timezone.make_aware(timezone.datetime(now.year, now.month, now.day, 23, 59, 59)) # obter a data e hora do final do dia atual
        if RegistroPonto.objects.filter(funcionario=request.user, data_hora__range=(start_of_day, end_of_day)).exists():
            registros_do_dia_atual = RegistroPonto.objects.filter(funcionario=request.user, data_hora__range=(start_of_day, end_of_day))
        else:
            registros_do_dia_atual = None

        if request.method == 'POST':
            form = RegistroPontoAdmin(request.POST)
            print(form.errors)
            if form.is_valid() and request.POST.get('action') == 'create':
                registro = form.save(commit=False)
                registro.funcionario = request.user
                # registra o tipo oposto ao último.
                registro.save()
                return redirect('admin')
        else:
            form = RegistroPontoAdmin()
        if not registros_do_dia_atual:
            return render(request, 'pontoAdmin.html', {'registros': '', 'horario_provavel_fim_turno': '', 'form':form})
        else: 
            saidas = []
            intervaloMinutos = 0
            
            for registro in registros_do_dia_atual:
                if registro.tipo == 'Saída':
                    saidas.append(registro.data_hora)
                else:
                    if saidas:
                        delta = registro.data_hora - saidas[-1]
                        intervaloMinutos += (delta.total_seconds() /60)
                    else:
                        intervaloMinutos = 0
            
            horario_provavel_fim_turno = registros_do_dia_atual[0].data_hora + timedelta(hours=8) + timedelta(minutes=intervaloMinutos)
            context = {'registros': registros_do_dia_atual, 'horario_provavel_fim_turno': horario_provavel_fim_turno, 'form':form}
            return render(request, 'pontoAdmin.html', context)
        
# def admin(request):
#     if not request.user.is_superuser:
#         raise PermissionDenied(
#             "You need administrator permissions for the time clock admin feature.")

#     now = timezone.now() # obter a data e hora atuais do timezone padrão
#     start_of_day = timezone.make_aware(timezone.datetime(now.year, now.month, now.day, 0, 0, 0)) # obter a data e hora do início do dia atual
#     end_of_day = timezone.make_aware(timezone.datetime(now.year, now.month, now.day, 23, 59, 59)) # obter a data e hora do final do dia atual
#     if RegistroPonto.objects.filter(funcionario=2, data_hora__range=(start_of_day, end_of_day)).exists():
#         registros_do_dia_atual = RegistroPonto.objects.filter(funcionario=2, data_hora__range=(start_of_day, end_of_day))
#     else:
#         registros_do_dia_atual = None
    

#     if request.method == 'POST':
#         form = RegistroPontoFormAdmin(request.POST)
#         if form.is_valid() and request.POST.get('action') == 'create':
#             registro = form.save(commit=False)
#             registro.funcionario = request.user
#             # registra o tipo oposto ao último.
#             registro.save()
#             return redirect('admin')
#         else:
#             form = RegistroPontoFormAdmin()
#     else:
#         context = {'registros': registros_do_dia_atual, 'form': form}
#         return render(request, 'pontoAdmin.html', context)
