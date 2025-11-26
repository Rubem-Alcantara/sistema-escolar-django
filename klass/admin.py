from django.contrib import admin

from .models import Aluno, Curso

# Registrando os modelos para aparecerem no painel
admin.site.register(Aluno)
admin.site.register(Curso)