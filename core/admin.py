from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente


class produtoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao", "quantidade", "preco")
    search_fields = ("nome", "descricao")

class clienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email", "telefone")
    search_fields = ("nome", "sobrenome", "email")


admin.site.register(Produto, produtoAdmin)
admin.site.register(Cliente, clienteAdmin)