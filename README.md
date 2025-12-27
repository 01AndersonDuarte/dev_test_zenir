# Dev Test Zenir

Dev Test Zenir é uma API desenvolvida em Python, com uso do FastAPI e SQLAlchemy, essa simples API possibilita o cadastro, a visualização, edição e exclusão de produtos gerais que contém campos básicos como preço e nome.

## Uso do FastAPI

O framework FastAPI foi escolhido para este projeto por possibilitar a criação de APIs modernas de forma simples, performática e bem estruturada. Ele disponibiliza tipagem estática com Python, validação automática de dados via Pydantic e geração automática de documentação interativa, como Swagger, o que facilita tanto o desenvolvimento quanto a manutenção da aplicação.

Além disso, o FastAPI possui excelente integração com o ecossistema Python, permitindo o uso de ORMs como o SQLAlchemy e garantindo um código mais legível, previsível e escalável.

## Arquitetura em camadas

Mesmo sendo um projeto de pequeno porte, foi aplicado o padrão de arquitetura em camadas com o intuito de dividir bem as responsabilidades de cada módulo da aplicação. Com essa abordagem temos uma base de código mais organizada, legível e de fácil manutenção.

A divisão em camadas permite maior escalabilidade ao longo do tempo, facilitando a evolução do sistema, a adição de novas funcionalidades e a implementação de um possível módulo de testes no futuro, sem impactar diretamente outras partes da aplicação.

## Uso do ORM SQLAlchemy

O ORM citado foi usado com o intuito de acelerar o mapeamento entre a aplicação e o banco de dados, facilitando a comunicação, a modelagem e a execução de operações de persistência de forma segura e eficiente. Além disso, o uso do SQLAlchemy contribui para a padronizar o acesso aos dados, centralizando as regras de persistência e permitindo maior controle sobre transações, integridade e consistência das informações, sem acoplamento direto às consultas SQL.

## Como executar a aplicação em sua máquina:

Para executar esta aplicação localmente, é necessário ter o **Python 3.10+** e o **PostgreSQL** instalados.

Você deverá criar um banco de dados PostgreSQL com o nome de sua preferência e configurar corretamente as variáveis de ambiente.

### Passo a passo

1. Clone o repositório:

```bash
git clone git@github.com:01AndersonDuarte/dev_test_zenir.git
cd dev_test_zenir
```

2. Renomeie o arquivo de variáveis de ambiente:

```bash
cp .env.example .env
```

3. Configure o arquivo .env com as credenciais do banco de dados PostgreSQL.

4. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

5. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

6. Execute a aplicação:

```bash
uvicorn src.main:app --reload
```

### Acessos

Após iniciar a aplicação, ela estará disponível nos seguintes endereços:

<ul>
    <li>API: <b>http://localhost:8000</b> </li>
    <li>Documentação Swagger: <b>http://localhost:8000/docs</b> </li>
    <li>Documentação ReDoc: <b>http://localhost:8000/redoc</b> </li>
</ul>

## Tecnologias utilizadas:

<div style="display: inline_block"><br>
    <img align="center" alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img align="center" alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
    <img align="center" alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
    <img align="center" alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
</div><br>
