# anuncio/admin.py

from django.contrib import admin
from .models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'preco', 'veiculo', 'usuario', 'criado_em', 'atualizado_em']
    search_fields = ['titulo', 'descricao', 'veiculo__modelo', 'usuario__username']
    list_filter = ['criado_em', 'atualizado_em']

admin.site.register(Anuncio, AnuncioAdmin)
