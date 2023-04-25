from django.urls import path
from . import views

urlpatterns = [
    #path('horas_extras/', views.horas_extras, name='horas_extras'),
    path('', views.dashboard, name='dashboard'),

]
