from django.contrib import admin
from .models import *

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    pass
