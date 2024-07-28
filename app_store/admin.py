from django.contrib import admin
from .models import Estado, Cidade, Endereco, Categoria, UnidadeMedida, Produto, Cliente, Venda, ItemVenda, Funcionario

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'sigla')

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'estado__nome')
    list_filter = ('estado',)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero', 'bairro', 'cep', 'cidade', 'criado_em', 'atualizado_em')
    search_fields = ('rua', 'bairro', 'cep', 'cidade__nome')
    list_filter = ('cidade',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo', 'criado_em', 'atualizado_em')
    search_fields = ('nome',)
    list_filter = ('ativo',)

@admin.register(UnidadeMedida)
class UnidadeMedidaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'criado_em', 'atualizado_em')
    search_fields = ('nome',)
    list_filter = ('ativo',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'custo', 'categoria', 'unidade_medida', 'ativo', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'descricao')
    list_filter = ('categoria', 'unidade_medida', 'ativo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_cliente', 'cpf', 'cnpj', 'contato', 'endereco', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'cpf', 'cnpj', 'contato')
    list_filter = ('tipo_cliente',)

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('data_venda', 'cliente', 'vendedor', 'criado_em', 'atualizado_em')
    search_fields = ('cliente__nome', 'vendedor__nome')
    list_filter = ('data_venda',)

@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'quantidade', 'preco_unitario', 'criado_em', 'atualizado_em')
    search_fields = ('venda__id', 'produto__nome')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'cargo', 'data_contratacao', 'endereco', 'ativo', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'contato', 'cargo')
    list_filter = ('cargo', 'ativo')
