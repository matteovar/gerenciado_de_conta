# Gerenciador de Gastos

Este é um aplicativo de gerenciamento de gastos pessoais desenvolvido com **Flask**, **SQLAlchemy** e **PostgreSQL**. Ele permite cadastrar, visualizar e remover despesas, além de gerar gráficos de gastos diários e por categoria utilizando **Plotly**.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **PostgreSQL**: Banco de dados relacional.
- **Plotly**: Biblioteca para gráficos interativos.
- **Python-dotenv**: Para carregar variáveis de ambiente.

## Funcionalidades

- Cadastro de despesas.
- Remoção de despesas.
- Visualização de gastos diários e por categoria.
- Gráficos interativos de gastos utilizando **Plotly**.

## Requisitos

Certifique-se de ter o seguinte instalado:

- **Python 3.x**
- **pip** (gerenciador de pacotes do Python)

### Instalando Dependências

Clone este repositório:

```
git clone https://github.com/seu-usuario/gerenciador-gastos.git

cd gerenciador-gastos
```
### Instalando Dependência

```
python -m venv venv
source venv/bin/activate  # no Linux ou MacOS
venv\Scripts\activate     # no Windows
```
### Instale as dependências:

```
pip install -r requirements.txt
```

### Configuração do Banco de Dados

1. Configure o PostgreSQL na nuvem:

    * Se estiver usando Render, Heroku ou outro serviço, crie uma instância de banco de dados PostgreSQL.

    * Copie a connection string fornecida (exemplo: postgresql://username:password@host:port/database).

2. Crie o arquivo .env:

    Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:

    ```bash
    DATABASE_URL=postgresql://username:password@host:port/database
    SECRET_KEY=sua_chave_secreta_aqui
    ```
    * Substitua DATABASE_URL pela string de conexão do seu banco de dados.

    * A chave secreta é usada para sessões e segurança do Flask.

### Rodando Localmente

Após configurar o banco de dados e o arquivo .env, inicie a aplicação localmente:

```
python app.py
```

Acesse o aplicativo no navegador:

```
http://127.0.0.1:5000/
```

# Estrutura do Projeto
```
gerenciador-gastos/
│
├── app.py                 # Arquivo principal da aplicação Flask.
├── models.py              # Definição dos modelos do banco de dados.
├── requirements.txt       # Dependências do Python.
├── .env.example           # Exemplo de arquivo .env (não comite o .env real).
│
├── templates/             # Arquivos HTML (ex: index.html).
├── static/                # Arquivos estáticos (CSS, JS).
│
└── README.md              # Este arquivo.
```

