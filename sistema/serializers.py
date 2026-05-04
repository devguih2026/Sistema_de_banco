from rest_framework import serializers
from .models import DadosPessoais, Banco, Contato, DadosFinanceiros, ContaBancaria, Cartao, Investimentos, Usuario

class DadosPessoaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = '__all__'


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'


class DadosFinanceirosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosFinanceiros
        fields = '__all__'


class ContaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaBancaria
        fields = '__all__'


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = '__all__'


class InvestimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investimentos
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


# Serializer completo — retorna todos os dados do cliente em uma única resposta
class ClienteCompletoSerializer(serializers.ModelSerializer):
    contato = ContatoSerializer(source='contato_set', many=True, read_only=True)
    dados_financeiros = DadosFinanceirosSerializer(source='dadosfinanceiros', read_only=True)
    contas_bancarias = ContaBancariaSerializer(source='contabancaria_set', many=True, read_only=True)
    cartoes = CartaoSerializer(source='cartao_set', many=True, read_only=True)
    investimentos = InvestimentosSerializer(source='investimentos_set', many=True, read_only=True)
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = DadosPessoais
        fields = '__all__'