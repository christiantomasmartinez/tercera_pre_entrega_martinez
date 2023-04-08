from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('mostrar-fecha/', views.mostrar_fecha, name='mostrar_fecha'),
    path('saludar/<str:nombre>/<str:apellido>/', views.saludar, name='saludar'),
    path('mi-primer-template/', views.mi_primer_template, name='mi_primer_template'),
    path('prueba-template/', views.prueba_template, name='prueba_template'),
    path('registrar-comprador/', views.registrar_comprador, name='registrar_comprador'),
    # path('registro-exitoso/', views.registro_exitoso, name='registro_exitoso'),
    # path('animales/', views.lista_animales, name='listar_animales'),
#     path('prueba-render/', views.prueba_render, name='prueba_render'),
 ]
