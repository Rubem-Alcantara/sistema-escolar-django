from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    
    # Relacionamento: Um aluno pode ter muitos cursos
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"