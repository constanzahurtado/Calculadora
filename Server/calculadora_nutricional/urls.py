from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('registro/', views.registro),
    path('login', views.login, name='login'),
    path('cerrar_sesion', views.cerrar_sesion),
    path('principal', views.principal),

]