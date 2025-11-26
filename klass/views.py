from django.shortcuts import render
from .models import Aluno, Curso

def index(request):
    # Contando os registros no banco
    total_alunos = Aluno.objects.count()
    total_cursos = Curso.objects.count()

    contexto = {
        'total_alunos': total_alunos,
        'total_cursos': total_cursos,
    }
    return render(request, 'klass/index.html', contexto)

# Função para exibir a lista de alunos
def lista_alunos(request):
    # 1. Buscando todos os objetos na tabela "Aluno" no banco de dados
    dados_alunos = Aluno.objects.all()
    
    # 2. Criando uma forme de encaminhar esses dados ao HTML
    contexto = {
        'lista_de_alunos': dados_alunos
    }
    
    # 3. Retorna a página renderizada usando o template HTML
    return render(request, 'klass/alunos.html', contexto)

# Função para exibir a lista de cursos
def lista_cursos(request):
    dados_cursos = Curso.objects.all()
    contexto = {
        'lista_de_cursos': dados_cursos
    }
    return render(request, 'klass/cursos.html', contexto)