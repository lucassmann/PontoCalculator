from django import forms
from funcionario.models import CustomUser


class UserDateForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    data_inicio = forms.DateField()
    data_fim = forms.DateField()
