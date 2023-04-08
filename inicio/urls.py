from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('mostrar-fecha/', views.mostrar_fecha, name='mostrar_fecha'),
    path('registrar-comprador/', views.registrar_comprador, name='registrar_comprador'),
    path('registrar-vendedor/', views.registrar_vendedor, name='registrar_vendedor'),
 ]
