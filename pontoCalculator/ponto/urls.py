from django.urls import path
from . import views

urlpatterns = [
    path('', views.ponto, name='ponto'),
    path('registrar_ponto', views.registrar_ponto, name='registrar_ponto'),
]
