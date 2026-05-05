from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import DadosPessoais

class DadosPessoaisTestCase(TestCase):

    def setUp(self):
        # Cria um usuário e autentica o client antes de cada teste
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        # Dado base reutilizado nos testes
        self.dados = {
            "nome": "João da Silva",
            "cpf": "123.456.789-00",
            "data_de_nascimento": "1990-05-15",
            "sexo": "M",
            "mae": "Maria da Silva",
            "estado_civil": "S",
            "nacionalidade": "Brasileiro"
        }

        # Cria um registro no banco para os testes que precisam de um existente
        self.cliente = DadosPessoais.objects.create(**self.dados)

    def test_criar_cliente(self):
        novos_dados = {
            "nome": "Maria Souza",
            "cpf": "987.654.321-00",
            "data_de_nascimento": "1995-08-20",
            "sexo": "F",
            "mae": "Ana Souza",
            "estado_civil": "S",
            "nacionalidade": "Brasileiro"
        }
        response = self.client.post('/clientes/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_clientes(self):
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detalhar_cliente(self):
        response = self.client.get(f'/clientes/{self.cliente.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.cliente.nome)

    def test_atualizar_cliente(self):
        dados_atualizados = {
            "nome": "João da Silva Atualizado",
            "cpf": "123.456.789-00",
            "data_de_nascimento": "1990-05-15",
            "sexo": "M",
            "mae": "Maria da Silva",
            "estado_civil": "C",
            "nacionalidade": "Brasileiro"
        }
        response = self.client.put(f'/clientes/{self.cliente.id}/', dados_atualizados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['estado_civil'], 'C')

    def test_deletar_cliente(self):
        response = self.client.delete(f'/clientes/{self.cliente.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_rejeitar_cpf_duplicado(self):
        response = self.client.post('/clientes/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejeitar_sem_jwt(self):
        client_sem_auth = APIClient()
        response = client_sem_auth.get('/clientes/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)