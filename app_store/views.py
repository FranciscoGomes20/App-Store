from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Estado, Cidade, Endereco, Categoria, UnidadeMedida, Produto, Cliente, Venda, ItemVenda, Funcionario
from .serializers import EstadoSerializer, CidadeSerializer, EnderecoSerializer, CategoriaSerializer, UnidadeMedidaSerializer, ProdutoSerializer, ClienteSerializer, VendaSerializer, ItemVendaSerializer, FuncionarioSerializer

class EstadoListCreateView(ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class EstadoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeListCreateView(ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class CidadeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class EnderecoListCreateView(ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EnderecoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class CategoriaListCreateView(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class UnidadeMedidaListCreateView(ListCreateAPIView):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer

class UnidadeMedidaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer

class ProdutoListCreateView(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ClienteListCreateView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VendaListCreateView(ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ItemVendaListCreateView(ListCreateAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class ItemVendaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class FuncionarioListCreateView(ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FuncionarioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
