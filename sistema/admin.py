from django.contrib import admin

from .models import DadosPessoais, Banco, Contato, DadosFinanceiros, ContaBancaria, Cartao, Investimentos, Usuario

admin.site.register(DadosPessoais)
admin.site.register(Banco)
admin.site.register(Contato)
admin.site.register(DadosFinanceiros)
admin.site.register(ContaBancaria)
admin.site.register(Cartao)
admin.site.register(Investimentos)
admin.site.register(Usuario)

