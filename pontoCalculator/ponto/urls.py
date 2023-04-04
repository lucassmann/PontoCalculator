from django.urls import path
from . import views

app_name = 'ponto'

urlpatterns = [
    path('', views.ponto, name='ponto'),
]
