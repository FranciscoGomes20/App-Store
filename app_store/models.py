from django.db import models
from django.core.exceptions import ValidationError

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.rua}, {self.numero}, {self.bairro}, {self.cidade}'

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data_pedido = models.DateTimeField()
    data_entrega = models.DateTimeField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pedido {self.id}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Item {self.id} do Pedido {self.pedido.id}'

class Cliente(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica')
    ]
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    tipo_cliente = models.CharField(max_length=2, choices=TIPO_CLIENTE_CHOICES)
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True, unique=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.tipo_cliente == 'PF' and not self.cpf:
            raise ValidationError('CPF é obrigatório para Pessoa Física.')
        if self.tipo_cliente == 'PJ' and not self.cnpj:
            raise ValidationError('CNPJ é obrigatório para Pessoa Jurídica.')
        if self.tipo_cliente == 'PF' and self.cnpj:
            raise ValidationError('CNPJ não deve ser preenchido para Pessoa Física.')
        if self.tipo_cliente == 'PJ' and self.cpf:
            raise ValidationError('CPF não deve ser preenchido para Pessoa Jurídica.')

    def __str__(self):
        return self.nome

class Venda(models.Model):
    data_venda = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Venda {self.id}'

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Item {self.id} da Venda {self.venda.id}'

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
