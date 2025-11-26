from django.urls import path
from . import views

urlpatterns = [
    # Chamando a função lista_alunos
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    # Chamando a função lista_cursos
    path('cursos/', views.lista_cursos, name='lista_cursos'),
]