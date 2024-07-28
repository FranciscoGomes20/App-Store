from django.urls import path
from .views import (
    EstadoListCreateView, EstadoDetailView,
    CidadeListCreateView, CidadeDetailView,
    EnderecoListCreateView, EnderecoDetailView,
    CategoriaListCreateView, CategoriaDetailView,
    UnidadeMedidaListCreateView, UnidadeMedidaDetailView,
    ProdutoListCreateView, ProdutoDetailView,
    ClienteListCreateView, ClienteDetailView,
    VendaListCreateView, VendaDetailView,
    ItemVendaListCreateView, ItemVendaDetailView,
    FuncionarioListCreateView, FuncionarioDetailView
)

urlpatterns = [
    path('estados/', EstadoListCreateView.as_view(), name='estado-list-create'),
    path('estados/<int:pk>/', EstadoDetailView.as_view(), name='estado-detail'),
    path('cidades/', CidadeListCreateView.as_view(), name='cidade-list-create'),
    path('cidades/<int:pk>/', CidadeDetailView.as_view(), name='cidade-detail'),
    path('enderecos/', EnderecoListCreateView.as_view(), name='endereco-list-create'),
    path('enderecos/<int:pk>/', EnderecoDetailView.as_view(), name='endereco-detail'),
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    path('unidades_medida/', UnidadeMedidaListCreateView.as_view(), name='unidademedida-list-create'),
    path('unidades_medida/<int:pk>/', UnidadeMedidaDetailView.as_view(), name='unidademedida-detail'),
    path('produtos/', ProdutoListCreateView.as_view(), name='produto-list-create'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('vendas/', VendaListCreateView.as_view(), name='venda-list-create'),
    path('vendas/<int:pk>/', VendaDetailView.as_view(), name='venda-detail'),
    path('itens_venda/', ItemVendaListCreateView.as_view(), name='itemvenda-list-create'),
    path('itens_venda/<int:pk>/', ItemVendaDetailView.as_view(), name='itemvenda-detail'),
    path('funcionarios/', FuncionarioListCreateView.as_view(), name='funcionario-list-create'),
    path('funcionarios/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionario-detail'),
]
