from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import ReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Estado, Cidade, Endereco, Categoria, UnidadeMedida, Produto, Cliente, Venda, ItemVenda, Funcionario
from .serializers import EstadoSerializer, CidadeSerializer, EnderecoSerializer, CategoriaSerializer, UnidadeMedidaSerializer, ProdutoSerializer, ClienteSerializer, VendaSerializer, ItemVendaSerializer, FuncionarioSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            if refresh_token is None:
                return Response({"error": "Refresh token não fornecido"}, status=400)
            
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logout realizado com sucesso"}, status=200)
        except Exception as e:
            return Response({"error": f"Falha no logout: {str(e)}"}, status=400)

class EstadoListCreateView(ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [ReadOnly]

class EstadoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [ReadOnly]

class CidadeListCreateView(ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [ReadOnly]

class CidadeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [ReadOnly]

class EnderecoListCreateView(ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [ReadOnly]

class EnderecoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [ReadOnly]

class CategoriaListCreateView(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [ReadOnly]

class CategoriaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [ReadOnly]

class UnidadeMedidaListCreateView(ListCreateAPIView):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer
    permission_classes = [ReadOnly]

class UnidadeMedidaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer
    permission_classes = [ReadOnly]

class ProdutoListCreateView(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [ReadOnly]

class ProdutoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [ReadOnly]

class ClienteListCreateView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [ReadOnly]

class ClienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [ReadOnly]

class VendaListCreateView(ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [ReadOnly]

class VendaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [ReadOnly]

class ItemVendaListCreateView(ListCreateAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer
    permission_classes = [ReadOnly]

class ItemVendaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer
    permission_classes = [ReadOnly]

class FuncionarioListCreateView(ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [ReadOnly]

class FuncionarioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [ReadOnly]
