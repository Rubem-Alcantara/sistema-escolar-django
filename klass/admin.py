from django.contrib import admin
from .models import Aluno, Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    # Barra de busca 
    search_fields = ('nome', 'sobrenome')
    # Paginação
    list_per_page = 20

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao_curta')
    search_fields = ('titulo',)

    def descricao_curta(self, obj):
        # Corta a descrição se for maior que 50 caracteres
        return obj.descricao[:50] + "..." if len(obj.descricao) > 50 else obj.descricao
    descricao_curta.short_description = 'Descrição'