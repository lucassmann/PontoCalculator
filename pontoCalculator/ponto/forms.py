from django import forms
from .models import RegistroPonto
from funcionario.models import CustomUser

class RegistroPontoForm(forms.ModelForm):
    class Meta:
        model = RegistroPonto
        
        exclude = ('funcionario','tipo', 'data_hora')


class RegistroPontoAdmin(forms.ModelForm):
    class Meta:
        model = RegistroPonto
        exclude = ('funcionario',)
        fields = ['data_hora', 'tipo', 'detalhes']
        


class UserDateForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    data = forms.DateField()