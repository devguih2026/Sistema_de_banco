from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import DadosPessoais, Banco, Contato, DadosFinanceiros, ContaBancaria, Cartao, Investimentos, Usuario
from .serializers import (
    DadosPessoaisSerializer, BancoSerializer, ContatoSerializer,
    DadosFinanceirosSerializer, ContaBancariaSerializer, CartaoSerializer,
    InvestimentosSerializer, UsuarioSerializer, ClienteCompletoSerializer
)
from .filters import (
    FiltroDadosPessoais, FiltroBanco, FiltroContato, FiltroDadosFinanceiros,
    FiltroContaBancaria, FiltroCartao, FiltroInvestimentos, FiltroUsuario
)

class DadosPessoaisViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FiltroDadosPessoais
    ordering_fields = ['nome', 'data_de_nascimento']
    ordering = ['nome']


class ClienteCompletoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DadosPessoais.objects.all()
    serializer_class = ClienteCompletoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FiltroDadosPessoais


class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FiltroBanco
    ordering_fields = ['nome']
    ordering = ['nome']


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FiltroContato


class DadosFinanceirosViewSet(viewsets.ModelViewSet):
    queryset = DadosFinanceiros.objects.all()
    serializer_class = DadosFinanceirosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FiltroDadosFinanceiros
    ordering_fields = ['renda_mensal', 'score_de_credito']
    ordering = ['-score_de_credito']


class ContaBancariaViewSet(viewsets.ModelViewSet):
    queryset = ContaBancaria.objects.all()
    serializer_class = ContaBancariaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FiltroContaBancaria
    ordering_fields = ['abertura_da_conta', 'saldo_atual']
    ordering = ['-abertura_da_conta']


class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FiltroCartao


class InvestimentosViewSet(viewsets.ModelViewSet):
    queryset = Investimentos.objects.all()
    serializer_class = InvestimentosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FiltroInvestimentos
    ordering_fields = ['valor_investido', 'data_de_aplicacao', 'rendimento_acumulado']
    ordering = ['-valor_investido']


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FiltroUsuario