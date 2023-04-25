from django import forms
from .models import RegistroPonto


class RegistroPontoForm(forms.ModelForm):
    class Meta:
        model = RegistroPonto
        
        exclude = ('funcionario','tipo', 'data_hora')


class RegistroPontoAdmin(forms.ModelForm):
    class Meta:
        model = RegistroPonto
        exclude = ('funcionario',)
        fields = ['data_hora', 'tipo', 'detalhes']
