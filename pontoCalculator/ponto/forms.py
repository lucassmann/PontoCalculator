from django import forms
from .models import RegistroPonto

class RegistroPontoForm(forms.ModelForm):
    
    class Meta:
        model = RegistroPonto
        exclude = ('funcionario','tipo')