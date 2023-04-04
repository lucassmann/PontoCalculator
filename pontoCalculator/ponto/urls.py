from django.urls import path
from . import views

urlpatterns = [
    path('', views.ponto, name='ponto'),
]
