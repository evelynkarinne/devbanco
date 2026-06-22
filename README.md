# DevBanco 💼

Um sistema web para gerenciar colaboradores e departamentos de uma organização, desenvolvido com **Flask** e **SQLAlchemy**.

## 📋 Sobre o Projeto

DevBanco é uma aplicação de recursos humanos (HR) que permite:
- Cadastrar e gerenciar **departamentos**
- Cadastrar, editar e excluir **colaboradores**
- Associar colaboradores a departamentos
- Visualizar dados de forma organizada

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|-----------|-----------|
| **Flask** | Framework web leve e poderoso para Python |
| **SQLAlchemy** | ORM para trabalhar com banco de dados |
| **Flask-Migrate** | Gerenciamento de migrações de banco de dados |
| **PostgreSQL** | Banco de dados relacional |
| **HTML/CSS** | Frontend da aplicação |

## 📊 Composição do Projeto

- **HTML** - 58.2%
- **Python** - 37.2%
- **CSS** - 4.6%

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8+
- PostgreSQL
- pip

### 1. Clonar o Repositório

```bash
git clone https://github.com/evelynkarinne/devbanco.git
cd devbanco
```

### 2. Criar um Ambiente Virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/devbanco
SECRET_KEY=sua_chave_secreta_aqui
FLASK_DEBUG=True
```

### 5. Executar a Aplicação

```bash
python app.py
```

Acesse em: `http://localhost:5000`

## 📁 Estrutura do Projeto

```
devbanco/
├── app.py              # Aplicação principal com rotas
├── config.py           # Configuração da aplicação
├── models.py           # Modelos de dados (Departamento, Colaborador)
├── requirements.txt    # Dependências do projeto
├── templates/          # Arquivos HTML
├── static/             # Arquivos CSS, JS e imagens
└── README.md          # Documentação
```

## 🔧 Principais Funcionalidades

### Rotas Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/departamentos` | GET | Listar departamentos |
| `/colaboradores` | GET | Listar colaboradores |
| `/novo-colaborador` | GET, POST | Criar novo colaborador |
| `/editar-colaborador/<id>` | GET, POST | Editar colaborador |
| `/excluir-colaborador/<id>` | GET | Excluir colaborador |

### Modelos de Dados

#### 📌 Departamento
```python
- codigo (int, PK)
- nome (string)
- sigla (string)
```

#### 👤 Colaborador
```python
- matricula (int, PK)
- nome (string)
- salario (decimal)
- email (string)
- endereco (string)
- codigo_dp (FK → Departamento)
```

## 📦 Dependências Principais

```
Flask==3.1.3
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.1.0
psycopg2-binary==2.9.12
python-dotenv==1.2.2
```

Para ver todas as dependências, consulte `requirements.txt`.

## 🔐 Segurança

- Chave secreta configurável via variáveis de ambiente
- Proteção contra SQL Injection com SQLAlchemy ORM
- Senhas devem ser implementadas em futuras versões

## 📝 Exemplos de Uso

### Criar um novo colaborador

```python
colaborador = Colaborador(
    matricula=1001,
    nome="João Silva",
    salario=3500.00,
    email="joao@example.com",
    endereco="Rua A, 123",
    codigo_dp=1
)
db.session.add(colaborador)
db.session.commit()
```

### Listar todos os colaboradores

```python
colaboradores = Colaborador.query.all()
for colab in colaboradores:
    print(colab.to_dict())
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👩‍💻 Autor

Desenvolvido por **evelynkarinne**

## 📧 Contato

Para dúvidas ou sugestões, abra uma [issue](https://github.com/evelynkarinne/devbanco/issues) no repositório.

---

**Desenvolvido com ❤️ para simplificar o gerenciamento de recursos humanos**
