from django.urls import path
from . import views

urlpatterns = [
    path('', views.ponto, name='ponto'),
    path('admin/registro', views.adminRegistro, name='admin_registro'),
    path('admin/', views.selecionar_usuario, name='admin')
]
