from django import forms
from .models import RegistroPonto
from django.contrib.admin.widgets import AdminSplitDateTime
from django.utils.translation import gettext_lazy as _
from datetime import datetime
class RegistroPontoForm(forms.ModelForm):
    class Meta:
        model = RegistroPonto
        
        exclude = ('funcionario','tipo', 'data_hora')


# class RegistroExcessaoForm(forms.ModelForm):
#     class Meta:
#         model = RegistroPonto
#         exclude = ('funcionario',)
#         fields = ['data_hora', 'tipo', 'detalhes']
#         widgets = {
#             'data_hora': AdminSplitDateTime(),
#         }
#         labels = {
#             'data_hora': _('Data e Hora'),
#             'tipo': _('Tipo'),
#             'detalhes': _('Detalhes'),
#         }

# from django import forms
# from django.forms import DateTimeInput
# from django.utils import timezone
# from .models import RegistroPonto


# class RegistroPontoForm(forms.ModelForm):
#     agora = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput())

#     class Meta:
#         model = RegistroPonto
#         fields = ['data_hora', 'tipo', 'detalhes']
#         widgets = {
#             'data_hora': DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={
#                 'placeholder': 'YYYY-MM-DD HH:MM:SS',
#                 'type': 'text',
#                 'autocomplete': 'off'
#             }),
#         }

#     def clean_data_hora(self):
#         data_hora = self.cleaned_data['data_hora']
#         if data_hora > timezone.now():
#             raise forms.ValidationError('Não é possível inserir data futura.')
#         return data_hora

#     def clean(self):
#         cleaned_data = super().clean()
#         agora = cleaned_data.get('agora')
#         data_hora = cleaned_data.get('data_hora')
#         if agora:
#             cleaned_data['data_hora'] = timezone.now()
#         return cleaned_data