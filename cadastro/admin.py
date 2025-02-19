from django.contrib import admin
from cadastro.models import Curso,Estudante
# Register your models here.

class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email','data_nascimento', 'celular', 'endereco')
    list_display_links = ('id', 'nome',)
    list_per_page = 20 
    search_fields = ('nome','cpf',)

admin.site.register(Estudante,Estudantes)