# 📚 DOCUMENTAÇÃO PEDAGÓGICA DO PROJETO
## Arquitetura de Software - Curso Python Rocketseat

---

**📅 Data de Geração:** 2025-11-27 12:14:06  
**🤖 Gerado por:** GitHub Copilot CLI - Agent AI  
**📌 Versão do Documento:** 1.0  
**🐍 Linguagem:** Python 3.12  
**🎯 Público-Alvo:** Estagiários e desenvolvedores iniciantes

---

## 📖 Sumário

1. [Introdução](#introdução)
2. [Diretórios Excluídos da Análise](#diretórios-excluídos-da-análise)
3. [Árvore de Diretórios](#árvore-de-diretórios)
4. [Análise por Pasta](#análise-por-pasta)
5. [Análise Detalhada dos Arquivos Python](#análise-detalhada-dos-arquivos-python)
6. [Comandos Úteis](#comandos-úteis)
7. [Checklist de Entendimento](#checklist-de-entendimento)
8. [Perguntas Sugeridas](#perguntas-sugeridas)
9. [Histórico de Geração](#histórico-de-geração)

---

## 🎯 Introdução

Este projeto é um exemplo didático de **arquitetura de software em Python** que implementa um sistema de gerenciamento de **pets e pessoas** usando SQLAlchemy como ORM (Object-Relational Mapping) e SQLite como banco de dados. O projeto segue o padrão **Repository Pattern** e demonstra boas práticas de organização de código, testes unitários e integração com banco de dados.

**Objetivo Pedagógico:** Ensinar conceitos de arquitetura em camadas, separação de responsabilidades, ORM, testes unitários com mocks e integração com banco de dados.

---

## 🚫 Diretórios Excluídos da Análise

Os seguintes diretórios foram excluídos desta documentação por serem arquivos gerados automaticamente ou configurações de ambiente:

- `__pycache__/` - Bytecode compilado do Python
- `venv/` e `.venv/` - Ambiente virtual Python
- `.git/` - Controle de versão Git
- `node_modules/` - Pacotes JavaScript (não aplicável aqui)
- `dist/` e `build/` - Distribuições compiladas
- `.pytest_cache/` - Cache do pytest (mencionado mas não detalhado)
- `.vscode/` - Configurações do VS Code (mencionado mas não detalhado)

---

## 🌳 Árvore de Diretórios

``
arquitetura_de_software/
│
├── 📄 .gitignore                    # Arquivos ignorados pelo Git
├── 📄 .pre-commit-config.yaml       # Configuração de hooks pre-commit
├── 📄 .pylintrc                     # Configuração do linter Pylint
├── 📄 ex_pylint.py                  # Exemplo simples para testar Pylint
├── 📄 requirements.txt              # Dependências do projeto
├── 🗄️  storage.db                   # Banco de dados SQLite (produção)
├── 🗄️  storage(backup).db           # Backup do banco de dados
│
├── 📂 init/
│   └── 📄 schema.sql                # Schema SQL para inicialização do BD
│
└── 📂 src/
    ├── 📄 __init__.py               # Pacote Python raiz
    │
    └── 📂 models/
        ├── 📄 __init__.py           # Pacote de modelos
        │
        └── 📂 sqlite/
            ├── 📄 __init__.py       # Pacote SQLite
            │
            ├── 📂 entities/         # Modelos ORM (Entidades)
            │   ├── 📄 __init__.py
            │   ├── 📄 people.py     # Entidade People
            │   └── 📄 pets.py       # Entidade PetsTable
            │
            ├── 📂 repositories/     # Camada de acesso a dados
            │   ├── 📄 __init__.py
            │   ├── 📄 pets_repository.py       # Repositório de Pets
            │   ├── �� pets_repository_test.py  # Testes unitários (mock)
            │   └── 📄 repositories_test.py     # Testes de integração
            │
            └── 📂 settings/         # Configurações de conexão
                ├── 📄 __init__.py
                ├── 📄 base.py                  # Base declarativa SQLAlchemy
                ├── 📄 connection.py            # Handler de conexão DB
                └── 📄 connection_test.py       # Testes de conexão
``

---
## 📂 Análise por Pasta

### 📂 Raiz do Projeto

**Propósito:** Contém arquivos de configuração do projeto, dependências, exemplos de uso e o banco de dados SQLite.

**Arquivos Principais:**
- `requirements.txt` - Lista de dependências Python
- `.pylintrc` - Configuração detalhada do linter
- `.pre-commit-config.yaml` - Hook para executar Pylint antes de commits
- `ex_pylint.py` - Exemplo básico para validar Pylint
- `storage.db` - Banco de dados SQLite em uso
- `.gitignore` - Arquivos/pastas ignorados pelo Git

**Notas Didáticas:**
- A raiz é o ponto de entrada e configuração do projeto
- Arquivos de configuração (`.pylintrc`, `.pre-commit-config.yaml`) garantem qualidade de código
- O banco de dados (`storage.db`) está na raiz para facilitar acesso - em projetos maiores, pode estar em outro local

---

### 📂 init/

**Propósito:** Contém scripts de inicialização do banco de dados, especialmente o schema SQL.

**Arquivos Principais:**
- `schema.sql` - Define estrutura das tabelas `pets` e `people` e insere dados iniciais

**Notas Didáticas:**
- Esta pasta é usada para setup inicial do projeto
- O schema SQL cria as tabelas e insere dados de exemplo
- Em produção, migrações de banco (como Alembic) seriam preferíveis

---

### 📂 src/

**Propósito:** Código-fonte principal do projeto. Contém toda a lógica de negócio e acesso a dados.

**Arquivos Principais:**
- `__init__.py` - Marca `src/` como pacote Python

**Dependências Internas:** 
- Contém subpacote `models/` que organiza toda a camada de dados

**Notas Didáticas:**
- A pasta `src/` é uma convenção comum em projetos Python
- Separar código em `src/` facilita importações e empacotamento
- Permite executar testes sem instalar o pacote

---

### 📂 src/models/

**Propósito:** Organiza todos os modelos de dados do projeto (entidades, repositórios, conexões).

**Arquivos Principais:**
- `__init__.py` - Marca como pacote Python

**Dependências Internas:**
- Contém subpacote `sqlite/` para implementação com SQLite

**Notas Didáticas:**
- A separação em `models/` permite adicionar outros bancos (PostgreSQL, MySQL) futuramente
- Segue o princípio de separação de responsabilidades

---

### 📂 src/models/sqlite/

**Propósito:** Implementação específica para SQLite, contendo entidades ORM, repositórios e configurações de conexão.

**Arquivos Principais:**
- `__init__.py` - Marca como pacote Python

**Dependências Internas:**
- `entities/` - Modelos ORM (mapeamento Python ↔ Tabelas)
- `repositories/` - Lógica de consultas e operações no banco
- `settings/` - Configuração de conexão e base do SQLAlchemy

**Notas Didáticas:**
- Organização em 3 camadas: Entidades (ORM), Repositórios (Queries) e Settings (Conexão)
- Padrão Repository separa lógica de negócio da persistência de dados

---

### 📂 src/models/sqlite/entities/

**Propósito:** Define as **entidades ORM** (modelos de dados) que mapeiam classes Python para tabelas do banco.

**Arquivos Principais:**
- `pets.py` - Classe `PetsTable` (tabela `pets`)
- `people.py` - Classe `People` (tabela `people`)
- `__init__.py` - Pacote Python

**Dependências Internas:**
- Importa `Base` de `settings.base` para herança
- Usa SQLAlchemy para mapeamento objeto-relacional

**Notas Didáticas:**
- **Entidades** representam as tabelas do banco como classes Python
- Cada atributo da classe corresponde a uma coluna da tabela
- Relacionamentos (Foreign Keys) estão definidos mas comentados

⚠️ **Ponto de Atenção:** A classe `People` tem um campo `type` que não está no schema SQL original - possível inconsistência.

---

### 📂 src/models/sqlite/repositories/

**Propósito:** Implementa o **padrão Repository**, que encapsula a lógica de acesso aos dados. Contém métodos para consultar, inserir, atualizar e deletar dados.

**Arquivos Principais:**
- `pets_repository.py` - Repositório com operações CRUD de pets
- `pets_repository_test.py` - Testes unitários usando mocks
- `repositories_test.py` - Testes de integração com banco real
- `__init__.py` - Pacote Python

**Dependências Internas:**
- Importa entidades de `entities/`
- Usa conexão de `settings/connection.py`
- Usa `mock-alchemy` para testes unitários

**Notas Didáticas:**
- **Repository Pattern** separa lógica de negócio da persistência
- Testes com mock não tocam o banco (rápidos e isolados)
- Testes de integração validam comportamento real (marcados com `skip`)

---

### 📂 src/models/sqlite/settings/

**Propósito:** Configurações de banco de dados, incluindo a base declarativa do SQLAlchemy e o handler de conexão.

**Arquivos Principais:**
- `base.py` - Define `Base` declarativa para ORM
- `connection.py` - Classe `DBConnectionHandler` para gerenciar conexões
- `connection_test.py` - Testes de conexão
- `__init__.py` - Pacote Python

**Dependências Internas:**
- `Base` é usado pelas entidades para herança
- `DBConnectionHandler` é usado pelos repositórios

**Notas Didáticas:**
- **Base declarativa** é o ponto central do ORM SQLAlchemy
- **Connection Handler** implementa Context Manager (`__enter__`, `__exit__`) para gerenciar sessões automaticamente
- Pattern Singleton usado para `db_connecition_handler`

---

## 🔍 Análise Detalhada dos Arquivos Python

---

### 📄 `ex_pylint.py`

**📍 Caminho:** `./ex_pylint.py`  
**📏 Linhas Totais:** 7  
**🎯 Propósito:** Arquivo de exemplo simples para testar a configuração do Pylint.

#### Resumo de Alto Nível
Este é um arquivo minimal usado para validar se o Pylint está funcionando corretamente com as configurações definidas em `.pylintrc`. Contém apenas uma função básica e uma chamada `print()`.

#### Dependências Internas
Nenhuma - arquivo standalone.

#### Código Completo com Explicação

``python
# L1-L7
print("Ola mundo")


def minha_funcao():
    """Minha função"""
    print("Estou na minha funcao")
``

**Explicação linha-a-linha:**

``python
print("Ola mundo")
``
- **L1:** Imprime "Ola mundo" no console. Nota: falta acento em "Olá" (intencional para exemplo).

``python


def minha_funcao():
``
- **L2-L3:** Linhas em branco para espaçamento (aceito pelo Pylint).
- **L4:** Define uma função chamada `minha_funcao` usando snake_case (convenção Python).

``python
    """Minha função"""
``
- **L5:** Docstring da função (documentação interna). O Pylint exige docstrings, mas está desabilitado no `.pylintrc` (C0116).

``python
    print("Estou na minha funcao")
``
- **L6:** Imprime mensagem indicando execução da função.

⚠️ **Observação:** A função `minha_funcao()` é definida mas nunca chamada. O código L1 executa diretamente, mas a função L4-L6 só executaria se fosse invocada.

---

### 📄 `src/__init__.py`

**📍 Caminho:** `./src/__init__.py`  
**📏 Linhas Totais:** 1 (vazio)  
**🎯 Propósito:** Marca a pasta `src/` como um pacote Python importável.

#### Resumo de Alto Nível
Arquivo vazio (`__init__.py`) que permite ao Python tratar a pasta `src/` como um módulo/pacote. Sem este arquivo, não seria possível fazer imports como `from src.models import ...`.

**Explicação:** Arquivos `__init__.py` podem ser vazios ou conter código de inicialização do pacote. Aqui está vazio, servindo apenas como marcador.

---
### 📄 `src/models/sqlite/entities/pets.py`

**📍 Caminho:** `./src/models/sqlite/entities/pets.py`  
**📏 Linhas Totais:** 18  
**🎯 Propósito:** Define a entidade ORM `PetsTable` que mapeia a tabela `pets` do banco de dados.

#### Resumo de Alto Nível
Esta classe representa a tabela `pets` usando SQLAlchemy ORM. Cada instância da classe é uma linha na tabela. Define colunas `id`, `name` e `type`, além de um relacionamento comentado com `People`.

#### Dependências Internas
- `Base` de `src.models.sqlite.settings.base` - Classe base para ORM
- SQLAlchemy: `Column`, `String`, `Integer` para definir colunas
- `relationship` (importado mas comentado no uso)

#### Código Completo com Explicação

``python
# L1-L18
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base

class PetsTable(Base):
    __tablename__ = "pets"
    
    id = Column(Integer, primary_key = True)
    name = Column(String,nullable=False)
    type = Column(String,nullable=False)
    
    # people = relationship('People',back_populates='pets')
    
    def __repr__(self):
        return f"PetsTable(name={self.name},type={self.type})"
``

**Explicação linha-a-linha:**

``python
from sqlalchemy import Column, String, Integer
``
- **L1:** Importa componentes do SQLAlchemy para definir colunas. `Column` define uma coluna, `String` e `Integer` são tipos de dados.

``python
from sqlalchemy.orm import relationship
``
- **L2:** Importa `relationship` para definir relacionamentos entre tabelas (foreign keys). Importado mas não usado atualmente.

``python
from src.models.sqlite.settings.base import Base
``
- **L3:** Importa `Base`, a classe declarativa que todas as entidades devem herdar. É o "contrato" com o SQLAlchemy.

``python
class PetsTable(Base):
``
- **L5:** Define classe `PetsTable` herdando de `Base`. Isso faz o SQLAlchemy reconhecer como tabela.

``python
    __tablename__ = "pets"
``
- **L6:** Atributo especial que define o nome da tabela no banco. SQLAlchemy usa isso para mapear.

``python
    id = Column(Integer, primary_key = True)
``
- **L8:** Define coluna `id` do tipo inteiro como chave primária. SQLAlchemy gerará automaticamente valores (AUTOINCREMENT).

``python
    name = Column(String,nullable=False)
``
- **L9:** Coluna `name` do tipo string (texto), obrigatória (`nullable=False`). Armazena o nome do pet.

``python
    type = Column(String,nullable=False)
``
- **L10:** Coluna `type` do tipo string, obrigatória. Armazena o tipo do pet (ex: "dog", "cat").

⚠️ **Observação:** Espaçamento inconsistente: `primary_key = True` tem espaços, mas `nullable=False` não. Preferível manter padrão.

``python
    # people = relationship('People',back_populates='pets')
``
- **L12:** Relacionamento comentado. Se ativado, criaria ligação bidirecional com a tabela `people`. `back_populates` sincroniza ambos os lados.

``python
    def __repr__(self):
        return f"PetsTable(name={self.name},type={self.type})"
``
- **L14-L15:** Método especial que define como o objeto é representado como string. Útil para debugging (ex: `print(pet)` mostra `PetsTable(name=dog,type=dog)`).

**⚠️ Possível Problema:** O `__repr__` não inclui `id`, que pode ser importante para debug.

---

### 📄 `src/models/sqlite/entities/people.py`

**📍 Caminho:** `./src/models/sqlite/entities/people.py`  
**📏 Linhas Totais:** 25  
**🎯 Propósito:** Define a entidade ORM `People` que mapeia a tabela `people` do banco de dados.

#### Resumo de Alto Nível
Representa a tabela `people` com informações de pessoas e suas relações com pets via foreign key `pet_id`.

#### Dependências Internas
- `Base` de `src.models.sqlite.settings.base`
- SQLAlchemy: `Column`, `String`, `Integer`, `ForeignKey`
- `relationship` (importado mas comentado)

#### Código Completo com Explicação

``python
# L1-L25
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base

class People(Base):
    __tablename__ = "people"
    
    id = Column(Integer, primary_key = True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    type = Column(String,nullable=False)
    
    pet_id = Column(Integer,ForeignKey('pets.id'))
    
    # pets = relationship('PetsTable',back_populates='people')
    
    def __repr__(self):
        return f"PetsTable(name={self.name},type={self.type})"
``

**Explicação linha-a-linha:**

``python
from sqlalchemy import Column, String, Integer,ForeignKey
``
- **L1:** Importa componentes do SQLAlchemy. `ForeignKey` define chaves estrangeiras (relacionamentos entre tabelas).

⚠️ **Observação:** Falta espaço após `Integer,` - inconsistência de estilo.

``python
class People(Base):
    __tablename__ = "people"
``
- **L5-L6:** Define classe `People` para tabela `people`.

``python
    id = Column(Integer, primary_key = True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
``
- **L8-L11:** Colunas básicas: ID (chave primária), primeiro nome, sobrenome e idade (todos obrigatórios).

``python
    type = Column(String,nullable=False)
``
- **L12:** Coluna `type` - **⚠️ PROBLEMA CRÍTICO:** Esta coluna NÃO existe no schema SQL (`init/schema.sql`). Isso causará erro ao tentar inserir/consultar pessoas.

``python
    pet_id = Column(Integer,ForeignKey('pets.id'))
``
- **L14:** Chave estrangeira que referencia `pets.id`. Vincula cada pessoa a um pet. `ForeignKey('pets.id')` cria a relação.

**Explicação Didática:** Foreign Key é como uma "seta" apontando de `people.pet_id` para `pets.id`, garantindo que cada pessoa tenha um pet válido.

``python
    # pets = relationship('PetsTable',back_populates='people')
``
- **L16:** Relacionamento comentado. Se ativo, permitiria acessar `pessoa.pets` para obter o objeto `PetsTable` relacionado.

``python
    def __repr__(self):
        return f"PetsTable(name={self.name},type={self.type})"
``
- **L21-L22:** **⚠️ ERRO CRÍTICO:** O `__repr__` tenta acessar `self.name` e `self.type`, mas a classe `People` não tem atributo `name`, apenas `first_name` e `last_name`. Isso causará `AttributeError` ao imprimir objetos. Além disso, diz `PetsTable` mas deveria ser `People`.

**⚠️ Problemas Identificados:**
1. Coluna `type` não existe no schema SQL
2. `__repr__` incorreto (copia/cola de `pets.py` sem adaptar)
3. `__repr__` diz `PetsTable` mas deveria ser `People`

---

### 📄 `src/models/sqlite/settings/base.py`

**📍 Caminho:** `./src/models/sqlite/settings/base.py`  
**📏 Linhas Totais:** 5  
**🎯 Propósito:** Define a classe `Base` declarativa do SQLAlchemy, base para todas as entidades ORM.

#### Resumo de Alto Nível
Cria e exporta a classe `Base` usando `declarative_base()`. Todas as entidades (PetsTable, People) herdam desta classe para serem reconhecidas pelo ORM.

#### Código Completo com Explicação

``python
# L1-L5
# from sqlalchemy.ext.declarative import declarative_base (old)
from sqlalchemy.orm import declarative_base

Base = declarative_base()
``

**Explicação linha-a-linha:**

``python
# from sqlalchemy.ext.declarative import declarative_base (old)
``
- **L1:** Comentário mostrando o import antigo do SQLAlchemy (versões < 1.4). Útil para referência histórica.

``python
from sqlalchemy.orm import declarative_base
``
- **L2:** Import correto para SQLAlchemy 2.x. `declarative_base()` cria a base para o sistema ORM.

``python
Base = declarative_base()
``
- **L4:** Cria instância de `Base`. Esta é a classe mãe que todas as entidades herdam. SQLAlchemy usa isso para mapear classes → tabelas.

**Explicação Didática:**  
Pense em `Base` como um "molde mágico". Toda classe que herda dela ganha poderes de ORM: SQLAlchemy automaticamente mapeia atributos para colunas, cria queries SQL e gerencia relacionamentos.

---
### 📄 `src/models/sqlite/settings/connection.py`

**📍 Caminho:** `./src/models/sqlite/settings/connection.py`  
**📏 Linhas Totais:** 27  
**🎯 Propósito:** Gerencia conexões com o banco de dados SQLite usando padrão Singleton e Context Manager.

#### Resumo de Alto Nível
Define a classe `DBConnectionHandler` que: (1) Cria engine de conexão com SQLite, (2) Gerencia sessões do banco (criar, usar, fechar), (3) Implementa Context Manager para uso com `with`, (4) Exporta instância singleton `db_connecition_handler`.

#### Código Completo com Explicação

``python
# L1-L27
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.session.close()

db_connecition_handler = DBConnectionHandler()
``

**Explicação linha-a-linha:**

``python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
``
- **L1-L2:** Importa ferramentas do SQLAlchemy: `create_engine` (cria engine de conexão) e `sessionmaker` (fabrica sessões/transações).

``python
class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None
``
- **L5-L9:** Construtor da classe. `__connection_string` é privado (`__`), define caminho do banco. `__engine` e `session` iniciam como `None`.

**Nota Didática:** Prefixo duplo `__` torna o atributo "privado" (name mangling), acessível apenas dentro da classe.

``python
    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)
``
- **L11-L12:** Cria engine de conexão. `create_engine` estabelece pool de conexões reutilizáveis.

**Explicação Didática:** Engine é como uma "fábrica de conexões". Não conecta imediatamente, mas gerencia pool de conexões.

``python
    def get_engine(self):
        return self.__engine
``
- **L14-L15:** Getter para acessar engine (privado). Usado em testes.

``python
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self
``
- **L17-L20:** Método especial para Context Manager (uso com `with`). Cria fábrica de sessões, cria sessão vinculada ao engine, retorna `self`.

**Explicação Didática:** Context Manager permite usar:
``python
with db_connecition_handler as db:
    db.session.query(...)  # Sessão aberta
# Ao sair do bloco, session fecha automaticamente (__exit__)
``

``python
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.session.close()
``
- **L22-L23:** Método chamado ao sair do bloco `with`. Fecha a sessão. Parâmetros de exceção não são usados.

``python
db_connecition_handler = DBConnectionHandler()
``
- **L26:** **Padrão Singleton** - Cria instância única global do handler, reutilizada em todo o código.

⚠️ **Observação:** Nome tem typo: `connecition` deveria ser `connection`.

**⚠️ Possível Problema:** A sessão nunca executa `rollback()` em caso de exceção. Deveria ter tratamento de erros.

---

### 📄 `src/models/sqlite/settings/connection_test.py`

**📍 Caminho:** `./src/models/sqlite/settings/connection_test.py`  
**📏 Linhas Totais:** 15  
**🎯 Propósito:** Testa a funcionalidade de conexão com o banco de dados.

#### Código Completo com Explicação

``python
# L1-L15
import pytest
from sqlalchemy.engine import Engine
from .connection import db_connecition_handler

# @pytest.mark.skip(reason='Interacao com o banco')
def test_connect_to_db():
    assert db_connecition_handler.get_engine() is None

    db_connecition_handler.connect_to_db()
    db_engine = db_connecition_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
``

**Explicação:**

- **L6:** Decorador comentado - teste **executa** normalmente (não está pulado).
- **L8:** Verifica que engine é `None` antes de conectar (estado inicial).
- **L10-L11:** Chama método de conexão e obtém engine.
- **L13-L14:** Verifica que engine existe e é do tipo correto.

**Fluxo:** ✅ Engine começa `None` → ✅ Após `connect_to_db()` existe → ✅ Tipo correto.

---

### 📄 `src/models/sqlite/repositories/pets_repository.py`

**📍 Caminho:** `./src/models/sqlite/repositories/pets_repository.py`  
**📏 Linhas Totais:** 33  
**🎯 Propósito:** Implementa o padrão Repository para operações CRUD na tabela `pets`.

#### Resumo de Alto Nível
Classe `PetsRepository` encapsula queries ao banco, oferecendo métodos de alto nível (`list_pets`, `delete_pets`). Separa lógica de acesso a dados da lógica de negócio.

#### Código Completo com Explicação

``python
# L1-L33
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable

class PetsRepository:
    def __init__(self,db_connection)-> None:
        self.__db_connection = db_connection
    
    def list_pets(self)-> List[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
    
    def delete_pets(self,name:str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
``

**Explicação por blocos:**

**Construtor (L7-L8):**
``python
def __init__(self,db_connection)-> None:
    self.__db_connection = db_connection
``
Recebe e armazena conexão como atributo privado.

**list_pets (L11-L18):**
``python
def list_pets(self)-> List[PetsTable]:
    with self.__db_connection as database:
        try:
            pets = database.session.query(PetsTable).all()
            return pets
        except NoResultFound:
            return []
``
- **L12:** Context Manager abre sessão automaticamente
- **L14:** Query equivalente a `SELECT * FROM pets`
- **L17-L18:** Retorna lista vazia se não encontrar (⚠️ `NoResultFound` nunca é lançado por `.all()`)

**delete_pets (L20-L32):**
``python
def delete_pets(self,name:str) -> None:
    with self.__db_connection as database:
        try:
            (
                database.session
                .query(PetsTable)
                .filter(PetsTable.name == name)
                .delete()
            )
            database.session.commit()
        except Exception as exception:
            database.session.rollback()
            raise exception
``
- **L24-L28:** Query de deleção: `DELETE FROM pets WHERE name = ?`
- **L29:** Commit confirma transação
- **L31-L33:** Rollback desfaz mudanças em caso de erro

**⚠️ Observações:**
1. `NoResultFound` em `list_pets` é desnecessário
2. `delete_pets` deleta todos os pets com o nome (se houver duplicatas)
3. Seria útil retornar número de pets deletados

---

### 📄 `src/models/sqlite/repositories/pets_repository_test.py`

**📍 Caminho:** `./src/models/sqlite/repositories/pets_repository_test.py`  
**📏 Linhas Totais:** 48  
**🎯 Propósito:** Testes unitários do `PetsRepository` usando **mocks** (sem tocar banco real).

#### Resumo de Alto Nível
Define classe `MockConnection` que simula conexão e testa `list_pets()` e `delete_pets()` verificando se queries corretas foram chamadas.

#### Código com Explicação

``python
# L1-L48
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],
                )
            ]
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()
    
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()
    
    assert response[0].name == "dog"

def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    
    repo.delete_pets("petName")
    
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == 'petName')
    mock_connection.session.delete.assert_called_once()
``

**MockConnection (L7-L25):**
Mock simula `DBConnectionHandler`. `UnifiedAlchemyMagicMock` cria "script" que quando `.query(PetsTable)` for chamado, retorna 2 pets pré-definidos sem tocar banco real.

**test_list_pets (L27-L37):**
Verifica que `query(PetsTable)` foi chamado 1 vez, `.all()` foi chamado, e `.filter()` NÃO foi chamado. Valida resultado retornado.

**test_delete_pet (L39-L48):**
Verifica que query, filter e delete foram chamados corretamente com parâmetros esperados.

**Explicação Didática:** Testes unitários verificam **como** o código funciona (quais métodos chama), não apenas **o que** retorna.

---

### 📄 `src/models/sqlite/repositories/repositories_test.py`

**📍 Caminho:** `./src/models/sqlite/repositories/repositories_test.py`  
**📏 Linhas Totais:** 18  
**🎯 Propósito:** Testes de **integração** com banco real (pulados por padrão).

#### Código

``python
# L1-L18
import pytest
from src.models.sqlite.settings.connection import db_connecition_handler
from .pets_repository import PetsRepository

db_connecition_handler.connect_to_db()

@pytest.mark.skip(reason='interacao com o banco')
def test_list_pets():
    repo = PetsRepository(db_connecition_handler)
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason='interacao com o banco')
def test_delete_pet():
    name = 'belinha'
    repo = PetsRepository(db_connecition_handler)
    repo.delete_pets(name=name)
``

**Explicação:**
- **L6:** Conecta ao banco antes dos testes
- **L8, L14:** Decorador pula testes (não executam por padrão)
- Testes usam banco **real** (`storage.db`)

⚠️ **Observação:** Não há asserções (`assert`) - apenas executam sem verificar resultado.

**Para executar:** `pytest -v` sem o skip ou `pytest --run-skipped`.

---
## 🛠️ Comandos Úteis

### Instalação de Dependências

``bash
# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
``

### Executar Testes

``bash
# Executar todos os testes (incluindo pulados)
pytest -v

# Executar apenas testes não-pulados
pytest -v -m "not skip"

# Executar testes de um arquivo específico
pytest src/models/sqlite/repositories/pets_repository_test.py -v

# Executar teste específico
pytest src/models/sqlite/repositories/pets_repository_test.py::test_list_pets -v

# Executar com cobertura
pytest --cov=src --cov-report=html
``

### Linting e Qualidade de Código

``bash
# Executar Pylint
pylint src/

# Executar Pylint em arquivo específico
pylint src/models/sqlite/entities/pets.py

# Executar pre-commit hooks manualmente
pre-commit run --all-files

# Instalar hooks do pre-commit (executa Pylint antes de commits)
pre-commit install
``

### Inicializar Banco de Dados

``bash
# Executar schema SQL (criar tabelas e dados iniciais)
sqlite3 storage.db < init/schema.sql

# Abrir console SQLite
sqlite3 storage.db

# Dentro do console SQLite:
.tables                 # Listar tabelas
SELECT * FROM pets;     # Consultar pets
SELECT * FROM people;   # Consultar pessoas
.exit                   # Sair
``

### Executar Python Interativo

``python
# Abrir console Python e testar código
python

# Dentro do console:
from src.models.sqlite.settings.connection import db_connecition_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository

db_connecition_handler.connect_to_db()
repo = PetsRepository(db_connecition_handler)
pets = repo.list_pets()
print(pets)
``

---

## ✅ Checklist de Entendimento

Após ler esta documentação, você deve ser capaz de:

- [ ] **Arquitetura:** Explicar a diferença entre Entities, Repositories e Settings
- [ ] **ORM:** Entender como `PetsTable` mapeia para tabela `pets` no banco
- [ ] **Repository Pattern:** Explicar por que `PetsRepository` separa lógica de negócio de acesso a dados
- [ ] **Context Manager:** Entender o uso de `with db_connecition_handler as database`
- [ ] **Testes Unitários:** Diferenciar testes com mock (`pets_repository_test.py`) de testes de integração (`repositories_test.py`)
- [ ] **SQLAlchemy:** Executar queries básicas usando `session.query()`
- [ ] **Foreign Keys:** Entender como `pet_id` em `People` relaciona com `id` em `PetsTable`
- [ ] **Singleton:** Identificar o padrão Singleton em `db_connecition_handler`
- [ ] **Debugging:** Saber como usar `__repr__` para debugar objetos
- [ ] **Configuração:** Entender o papel de `.pylintrc` e `requirements.txt`

---

## ❓ Perguntas Sugeridas

Para aprofundar seu conhecimento, explore estas questões:

1. **Fluxo de Dados:** Como um dado flui desde uma chamada `repo.list_pets()` até retornar objetos `PetsTable`? Desenhe o caminho.

2. **Testes:** Por que usamos mocks em `pets_repository_test.py` em vez de banco real? Quais são as vantagens e desvantagens?

3. **Relacionamentos:** Se descomentássemos `relationship()` em `pets.py` e `people.py`, como acessaríamos o pet de uma pessoa? E todas as pessoas de um pet?

4. **Erros Identificados:** Como você corrigiria o `__repr__` da classe `People` e o campo `type` extra?

5. **Expansão:** Como você adicionaria um método `insert_pet(name, type)` ao `PetsRepository`? Escreva o código e um teste unitário.

6. **Transações:** O que aconteceria se removêssemos `database.session.commit()` de `delete_pets()`? Por quê?

---

## ⚠️ Problemas Identificados e Melhorias Sugeridas

### Problemas Críticos

1. **`people.py` - Linha 12:**  
   ❌ Coluna `type` não existe no schema SQL (`init/schema.sql`). Remover ou adicionar ao schema.

2. **`people.py` - Linha 21-22:**  
   ❌ `__repr__` acessa `self.name` inexistente e retorna `"PetsTable(...)"` em vez de `"People(...)"`

### Problemas Moderados

3. **`pets_repository.py` - Linha 17:**  
   ⚠️ `except NoResultFound` nunca executará (`.all()` não lança essa exceção)

4. **`connection.py` - Linha 26:**  
   ⚠️ Nome com typo: `db_connecition_handler` → `db_connection_handler`

5. **`connection.py` - Linha 23:**  
   ⚠️ `__exit__` não trata rollback em caso de exceção

### Melhorias Sugeridas

6. **Testes de Integração:**  
   💡 Adicionar asserções em `repositories_test.py` para validar resultados

7. **Validação:**  
   💡 `delete_pets()` deveria verificar se pet existe e retornar número de deletados

8. **Type Hints:**  
   💡 Adicionar type hints completos em todas as funções

9. **Documentação:**  
   💡 Adicionar docstrings em métodos para melhor documentação

10. **Espaçamento:**  
    💡 Padronizar espaçamento em parâmetros de funções e argumentos

---

## 📋 Histórico de Geração

| Versão | Data | Observações |
|--------|------|-------------|
| 1.0 | 2025-11-27 12:14:06 | Geração inicial da documentação pedagógica completa |

---

## 📊 Sumário Executivo

### Arquivos Críticos
O projeto possui **3 arquivos principais** que formam o núcleo da aplicação:
1. `connection.py` - Gerencia todas as conexões com o banco de dados
2. `pets_repository.py` - Implementa lógica de acesso aos dados de pets
3. `pets.py` e `people.py` - Definem o modelo de dados (ORM)

### Dependências Principais
- **SQLAlchemy 2.0.44** - ORM para mapeamento objeto-relacional
- **pytest 9.0.1** - Framework de testes
- **mock-alchemy 0.2.6** - Biblioteca para mockar SQLAlchemy em testes
- **pylint 4.0.2** - Linter para qualidade de código
- **pre-commit 4.4.0** - Hooks para executar linters antes de commits

### Como Rodar
1. Criar ambiente virtual: `python -m venv venv`
2. Ativar: `venv\Scripts\activate` (Windows)
3. Instalar dependências: `pip install -r requirements.txt`
4. Inicializar BD: `sqlite3 storage.db < init/schema.sql`
5. Executar testes: `pytest -v`

### Riscos e Observações Importantes

**⚠️ Risco 1 - Inconsistência no Schema:**  
A classe `People` define uma coluna `type` que não existe no schema SQL (`init/schema.sql`). Isso causará erros ao tentar inserir ou consultar pessoas. **Ação necessária:** Remover coluna `type` de `people.py` ou adicionar ao schema.

**⚠️ Risco 2 - `__repr__` Quebrado:**  
O método `__repr__` da classe `People` tenta acessar `self.name` (que não existe) e retorna `"PetsTable"` em vez de `"People"`. Isso causará `AttributeError` ao tentar imprimir objetos `People`. **Ação necessária:** Corrigir para usar `first_name` e `last_name`.

---

## 🎓 Dica Final para Estagiários

Este projeto é um excelente exemplo de **arquitetura em camadas**. Estude cada camada separadamente:

1. **Settings** → Configuração e conexão com banco
2. **Entities** → Modelos de dados (mapeamento Python ↔ Tabelas)
3. **Repositories** → Lógica de acesso a dados (queries)

Depois, veja como elas se conectam! Pratique modificando o código e executando os testes. Comece pelos testes unitários (com mocks) para entender o comportamento esperado, depois explore os testes de integração.

**Analogia útil:** Pense no projeto como uma biblioteca:
- **Entities** são as fichas catalográficas (definem o que é cada livro)
- **Repositories** são os bibliotecários (buscam, organizam, removem livros)
- **Settings** é a infraestrutura (prédio, sistema de organização)

---

**📝 Notas de Segurança:**  
- Banco de dados (`storage.db`) contém dados de exemplo - não há informações sensíveis
- Não há arquivo `.env` detectado neste projeto
- String de conexão está hardcoded em `connection.py` (aceitável para projetos educacionais, mas em produção use variáveis de ambiente)

---

**Fim da Documentação** 🎉

---

**Gerado automaticamente por GitHub Copilot CLI**  
Para dúvidas ou sugestões, consulte a documentação do SQLAlchemy em https://docs.sqlalchemy.org/
