import django_filters
from .models import DadosPessoais, Contato, DadosFinanceiros, ContaBancaria, Cartao, Investimentos, Usuario, Banco

class FiltroDadosPessoais(django_filters.FilterSet):
    # exemplo: GET http://localhost:8000/clientes/?nome=João
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains')
    cpf = django_filters.CharFilter(field_name='cpf', lookup_expr='exact')
    sexo = django_filters.ChoiceFilter(field_name='sexo', choices=[('M', 'Masculino'), ('F', 'Feminino')])
    estado_civil = django_filters.ChoiceFilter(field_name='estado_civil', choices=[('S', 'Solteiro(a)'), ('N', 'Namorando'), ('C', 'Casado(a)')])
    nacionalidade = django_filters.CharFilter(field_name='nacionalidade', lookup_expr='icontains')

    class Meta:
        model = DadosPessoais
        fields = ['nome', 'cpf', 'sexo', 'estado_civil', 'nacionalidade']


class FiltroUsuario(django_filters.FilterSet):
    status_da_conta = django_filters.ChoiceFilter(field_name='status_da_conta', choices=[('A', 'Ativa'), ('E', 'Encerrada'), ('B', 'Bloqueada')])

    class Meta:
        model = Usuario
        fields = ['status_da_conta']


class FiltroContato(django_filters.FilterSet):
    cidade = django_filters.CharFilter(field_name='cidade', lookup_expr='icontains')
    estado = django_filters.CharFilter(field_name='estado', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = Contato
        fields = ['cidade', 'estado', 'email']


class FiltroDadosFinanceiros(django_filters.FilterSet):
    score_de_credito_min = django_filters.NumberFilter(field_name='score_de_credito', lookup_expr='gte')
    score_de_credito_max = django_filters.NumberFilter(field_name='score_de_credito', lookup_expr='lte')
    renda_mensal_min = django_filters.NumberFilter(field_name='renda_mensal', lookup_expr='gte')
    renda_mensal_max = django_filters.NumberFilter(field_name='renda_mensal', lookup_expr='lte')

    class Meta:
        model = DadosFinanceiros
        fields = ['score_de_credito_min', 'score_de_credito_max', 'renda_mensal_min', 'renda_mensal_max']


class FiltroContaBancaria(django_filters.FilterSet):
    tipo_de_conta = django_filters.ChoiceFilter(field_name='tipo_de_conta', choices=[('C', 'Corrente'), ('P', 'Poupança'), ('S', 'Salário')])
    agencia = django_filters.CharFilter(field_name='agencia', lookup_expr='exact')
    numero_da_conta = django_filters.CharFilter(field_name='numero_da_conta', lookup_expr='exact')

    class Meta:
        model = ContaBancaria
        fields = ['tipo_de_conta', 'agencia', 'numero_da_conta']


class FiltroCartao(django_filters.FilterSet):
    bandeira = django_filters.ChoiceFilter(field_name='bandeira', choices=[('V', 'Visa'), ('M', 'Mastercard'), ('E', 'Elo'), ('A', 'American Express'), ('H', 'Hipercard')])
    tipo = django_filters.ChoiceFilter(field_name='tipo', choices=[('C', 'Crédito'), ('D', 'Débito'), ('A', 'Ambos')])

    class Meta:
        model = Cartao
        fields = ['bandeira', 'tipo']


class FiltroInvestimentos(django_filters.FilterSet):
    tipo = django_filters.ChoiceFilter(field_name='tipo', choices=[('RF', 'Renda Fixa'), ('RV', 'Renda Variável'), ('E', 'Exterior'), ('C', 'Cripto')])
    valor_investido_min = django_filters.NumberFilter(field_name='valor_investido', lookup_expr='gte')
    valor_investido_max = django_filters.NumberFilter(field_name='valor_investido', lookup_expr='lte')
    data_de_aplicacao = django_filters.DateFilter(field_name='data_de_aplicacao', lookup_expr='exact')

    class Meta:
        model = Investimentos
        fields = ['tipo', 'valor_investido_min', 'valor_investido_max', 'data_de_aplicacao']


class FiltroBanco(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains')

    class Meta:
        model = Banco
        fields = ['nome']

        # python manage.py makemigrations

        # python manage.py migrate