from django.db import models

class DadosPessoais(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, blank=False, null=False)
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    mae = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=1, choices=[('S', 'Solteiro(a)'), ('N', 'Namorando'), ('C', 'Casado(a)')])
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Banco(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    id_cliente = models.OneToOneField(DadosPessoais, on_delete=models.CASCADE)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=False, null=False)
    cep = models.CharField(max_length=9, verbose_name="CEP")
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

class DadosFinanceiros(models.Model):
    id_cliente = models.OneToOneField(DadosPessoais, on_delete=models.CASCADE)
    renda_mensal = models.DecimalField(max_digits=15, decimal_places=2)
    score_de_credito = models.IntegerField()
    limite_de_credito_total = models.DecimalField(max_digits = 15, decimal_places= 2)
    limite_disponivel = models.DecimalField(max_digits = 15, decimal_places= 2)

class ContaBancaria(models.Model):
    id_cliente = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    id_banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    numero_da_conta = models.CharField(max_length=14, unique=True, blank=False, null=False)
    agencia = models.CharField(max_length=14, blank=False, null=False)
    tipo_de_conta = models.CharField(max_length=1, choices=[('C', 'Corrente'), ('P', 'Poupança'), ('S', 'Salário')]) # (corrente, poupança, salário)
    saldo_atual = models.DecimalField(max_digits=15, decimal_places=2)
    abertura_da_conta = models.DateField()

class Cartao(models.Model):
    id_cliente = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    id_banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    numero_do_cartao = models.CharField(max_length=19) #(tokenizado)
    bandeira = models.CharField(max_length=2, choices=[('V', 'Visa'), ('M', 'Mastercard'), ('E', 'Elo'), ('AE', 'American Express'), ('H', 'Hipercard')]) 
    limite = models.DecimalField(max_digits=15, decimal_places=2)
    data_de_vencimento = models.DateField()
    tipo = models.CharField(max_length=1, choices=[('C', 'crédito'), ('D', 'débito'), ('A', 'ambos')])  

class Investimentos(models.Model):
    id_cliente = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=2, choices=[('RF', 'Renda Fixa'), ('RV', 'Renda variável'), ('E', 'Exterior'), ('C', 'Cripto')])  
    valor_investido = models.DecimalField(max_digits=15, decimal_places=2)
    rendimento_acumulado = models.DecimalField(max_digits=15, decimal_places=2)
    data_de_aplicacao = models.DateField()
    data_de_vencimento = models.DateField(null=True, blank=True)

class Usuario(models.Model):
    id_cliente = models.OneToOneField(DadosPessoais, on_delete=models.CASCADE)
    data_de_cadastro = models.DateTimeField(auto_now_add=True)
    status_da_conta = models.CharField(max_length=1, choices=[('A', 'Ativa'), ('E', 'Encerrada'), ('B', 'Bloqueada')])   # (ativa, bloqueada, encerrada)
    ultimo_acesso = models.DateTimeField(auto_now=True)

