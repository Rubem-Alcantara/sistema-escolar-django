# Sistema Escolar - Django

Projeto desenvolvido para a disciplina de Programação Backend. O objetivo foi criar um sistema de gestão de alunos e cursos utilizando o framework Django.

<img width="1920" height="966" alt="image" src="https://github.com/user-attachments/assets/d105113d-4625-4a6e-a17b-a32b96c1da38" />

## 🚀 Tecnologias Usadas
* Python 3.12
* Django 5.2
* Bootstrap 5
* SQLite

## 📋 Funcionalidades
* Cadastro de Alunos e Cursos (Admin)
* Relacionamento Muitos-para-Muitos (Um aluno pode ter vários cursos)
* Dashboard com estatísticas
* Interface responsiva

## 🔧 Como rodar o projeto
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o venv e instale o Django: `pip install django`
4. Execute as migrações: `python manage.py migrate`
5. Crie um superusuário: `python manage.py createsuperuser`
6. Rode o servidor: `python manage.py runserver`
