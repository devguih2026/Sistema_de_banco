# 🏦 Sistema_banco

Sistema backend de simulação de dados de clientes bancários, desenvolvido com Django e MySQL. O projeto simula funcionalidades de bancos digitais como Nubank, Inter, C6, Bradesco, entre outros.

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Executando o Projeto](#executando-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Endpoints da API](#endpoints-da-api)
- [Autenticação](#autenticação)
- [Documentação Swagger](#documentação-swagger)
- [Modelos de Dados](#modelos-de-dados)

---

## 📌 Sobre o Projeto

O **Sistema_banco** é uma API REST backend que simula o gerenciamento de dados de clientes bancários. O sistema permite o cadastro e gerenciamento de clientes, contas bancárias, cartões, transações e investimentos, com autenticação via JWT.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Django** — Framework web
- **Django REST Framework** — Construção da API REST
- **djangorestframework-simplejwt** — Autenticação JWT
- **drf-spectacular** — Documentação Swagger/OpenAPI
- **MySQL** — Banco de dados relacional
- **mysqlclient** — Conector MySQL para Python
- **python-decouple** — Gerenciamento de variáveis de ambiente

---

## ✅ Requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.10 ou superior
- MySQL Server
- pip (gerenciador de pacotes Python)
- Git

---

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/sistema_banco.git
cd sistema_banco
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

- **Windows:**
```bash
venv\Scripts\activate
```

- **Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Atualize o pip

```bash
pip install --upgrade pip
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

### 1. Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no arquivo `.env.example`:

```bash
cp .env.example .env
```

Preencha as variáveis no arquivo `.env`:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True

DB_NAME=sistema_banco
DB_USER=seu-usuario-mysql
DB_PASSWORD=sua-senha-mysql
DB_HOST=localhost
DB_PORT=3306
```

### 2. Crie o banco de dados no MySQL

```sql
CREATE DATABASE sistema_banco CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Execute as migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

---

## ▶️ Executando o Projeto

```bash
python manage.py runserver
```

A API estará disponível em: `http://localhost:8000`

---

## 🔗 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/token/` | Obter token JWT |
| POST | `/api/token/refresh/` | Renovar token JWT |
| GET/POST | `/api/customers/` | Listar/criar clientes |
| GET/PUT/DELETE | `/api/customers/{id}/` | Detalhar/editar/deletar cliente |
| GET/POST | `/api/banks/` | Listar/criar bancos |
| GET/POST | `/api/bank-accounts/` | Listar/criar contas bancárias |
| GET/POST | `/api/transactions/` | Listar/criar transações |
| GET/POST | `/api/cards/` | Listar/criar cartões |
| GET/POST | `/api/investments/` | Listar/criar investimentos |

---

## 🔐 Autenticação

O sistema utiliza autenticação **JWT (JSON Web Token)**.

### Obtendo o token

```http
POST /api/token/
Content-Type: application/json

{
  "username": "seu-usuario",
  "password": "sua-senha"
}
```

### Utilizando o token nas requisições

```http
GET /api/customers/
Authorization: Bearer <seu-token-aqui>
```

### Renovando o token

```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "seu-refresh-token"
}
```

---

## 📖 Documentação Swagger

A documentação interativa da API está disponível em:

- **Swagger UI:** `http://localhost:8000/api/schema/swagger-ui/`
- **Redoc:** `http://localhost:8000/api/schema/redoc/`
- **Schema OpenAPI:** `http://localhost:8000/api/schema/`

---

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
