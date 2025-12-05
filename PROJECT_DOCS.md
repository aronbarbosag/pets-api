# 📚 DOCUMENTAÇÃO PEDAGÓGICA DO PROJETO

## Arquitetura de Software - Curso Python Rocketseat

---

**📅 Data de Geração:** 2025-12-02 12:00:00  
**🤖 Gerado por:** GitHub Copilot - Agent AI (Claude Opus 4.5)  
**📌 Versão do Documento:** 2.0  
**🐍 Linguagem:** Python 3.12  
**🎯 Público-Alvo:** Estagiários e desenvolvedores iniciantes

---

## 📖 Sumário

1. [Introdução](#-introdução)
2. [Diretórios Excluídos da Análise](#-diretórios-excluídos-da-análise)
3. [Árvore de Diretórios](#-árvore-de-diretórios)
4. [Arquivos da Raiz](#-arquivos-da-raiz)
5. [Pasta init/](#-pasta-init)
6. [Pasta src/](#-pasta-src)
7. [Pasta src/controllers/](#-pasta-srccontrollers)
8. [Pasta src/controllers/interfaces/](#-pasta-srccontrollersinterfaces)
9. [Pasta src/models/](#-pasta-srcmodels)
10. [Pasta src/models/sqlite/entities/](#-pasta-srcmodelssqliteentities)
11. [Pasta src/models/sqlite/interfaces/](#-pasta-srcmodelssqliteinterfaces)
12. [Pasta src/models/sqlite/repositories/](#-pasta-srcmodelssqliterepositories)
13. [Pasta src/models/sqlite/settings/](#-pasta-srcmodelssqlitesettings)
14. [Comandos Úteis](#-comandos-úteis)
15. [Checklist de Entendimento](#-checklist-de-entendimento)
16. [Perguntas Sugeridas](#-perguntas-sugeridas)
17. [Histórico de Geração](#-histórico-de-geração)

---

## 🎯 Introdução

Este projeto é um exemplo didático de **arquitetura de software em Python** que implementa um sistema de gerenciamento de **pets e pessoas** usando:

- **SQLAlchemy** como ORM (Object-Relational Mapping)
- **SQLite** como banco de dados
- **Padrão Repository** para abstração de acesso a dados
- **Interfaces (ABC)** para contratos entre camadas
- **Pytest** para testes unitários

**Analogia Pedagógica:** Imagine o projeto como um restaurante:

- `controllers/` = garçons (recebem pedidos e entregam respostas)
- `repositories/` = cozinha (prepara/busca os dados)
- `entities/` = cardápio (define a estrutura dos "pratos"/dados)
- `interfaces/` = manual de operações (regras que todos devem seguir)

---

## 🚫 Diretórios Excluídos da Análise

Os seguintes diretórios foram excluídos desta documentação:

| Diretório        | Motivo                                                |
| ---------------- | ----------------------------------------------------- |
| `__pycache__/`   | Bytecode compilado do Python (gerado automaticamente) |
| `venv/`          | Ambiente virtual Python                               |
| `.venv/`         | Ambiente virtual Python (alternativo)                 |
| `.git/`          | Controle de versão Git                                |
| `.pytest_cache/` | Cache do pytest                                       |
| `.vscode/`       | Configurações da IDE                                  |

---

## 🌳 Árvore de Diretórios

```
arquitetura_de_software/
├── 📄 ex_pylint.py                          # Exemplo básico de Python
├── 📄 PROJECT_DOCS.md                       # Esta documentação
├── 📄 requirements.txt                      # Dependências do projeto
│
├── 📁 init/
│   └── 📄 schema.sql                        # Script de criação do banco
│
└── 📁 src/                                  # Código-fonte principal
    ├── 📄 __init__.py
    │
    ├── 📁 controllers/                      # Camada de controle
    │   ├── 📄 __init__.py
    │   ├── 📄 person_creator_controller.py
    │   ├── 📄 person_creator_controller_test.py
    │   ├── 📄 person_finder_controller.py
    │   ├── 📄 person_finder_controller_test.py
    │   ├── 📄 pet_deleter_controller.py
    │   ├── 📄 pet_deleter_controller_test.py
    │   ├── 📄 pet_lister_controller.py
    │   ├── 📄 pet_lister_controller_test.py
    │   ├── 📄 pets_creator_controller.py
    │   │
    │   └── 📁 interfaces/                   # Contratos dos controllers
    │       ├── 📄 __init__.py
    │       ├── 📄 person_creator_controller.py
    │       ├── 📄 person_finder_controller.py
    │       ├── 📄 pet_deleter_controller.py
    │       └── 📄 pet_lister_controller.py
    │
    └── 📁 models/                           # Camada de dados
        ├── 📄 __init__.py
        │
        └── 📁 sqlite/                       # Implementação SQLite
            ├── 📄 __init__.py
            │
            ├── 📁 entities/                 # Entidades/Tabelas
            │   ├── 📄 __init__.py
            │   ├── 📄 people.py
            │   └── 📄 pets.py
            │
            ├── 📁 interfaces/               # Contratos dos repositories
            │   ├── 📄 __init__.py
            │   ├── 📄 people_repository.py
            │   └── 📄 pets_repository.py
            │
            ├── 📁 repositories/             # Implementação dos repositories
            │   ├── 📄 __init__.py
            │   ├── 📄 people_repository.py
            │   ├── 📄 pets_repository.py
            │   ├── 📄 pets_repository_test.py
            │   └── 📄 repositories_test.py
            │
            └── 📁 settings/                 # Configurações do banco
                ├── 📄 __init__.py
                ├── 📄 base.py
                ├── 📄 connection.py
                └── 📄 connection_test.py
```

---

## 📁 Arquivos da Raiz

### 📄 `requirements.txt`

**Caminho:** `./requirements.txt`  
**Propósito:** Lista todas as dependências (bibliotecas) necessárias para o projeto funcionar.

**Dependências Principais:**
| Pacote | Versão | Função |
|--------|--------|--------|
| `SQLAlchemy` | 2.0.44 | ORM para banco de dados |
| `pytest` | 9.0.1 | Framework de testes |
| `mock-alchemy` | 0.2.6 | Mocks para SQLAlchemy em testes |
| `pylint` | 4.0.2 | Analisador de código |
| `pre_commit` | 4.4.0 | Hooks de pré-commit |

---

### 📄 `ex_pylint.py`

**Caminho:** `./ex_pylint.py` | **Linhas:** 7  
**Propósito:** Arquivo de exemplo simples para demonstrar boas práticas de Python com Pylint.

```python
# L1-L7 - ./ex_pylint.py
print("Ola mundo")                    # L1: Imprime uma saudação simples no console


def minha_funcao():                   # L4: Define uma função chamada "minha_funcao"
    """Minha função"""                # L5: Docstring - documentação obrigatória para funções (boa prática)
    print("Estou na minha funcao")    # L6: Imprime mensagem quando a função é chamada
```

**📝 Notas Didáticas:**

- A docstring (linha 5) é obrigatória pelo Pylint para documentar funções
- Este arquivo serve como exemplo mínimo de código que passa na validação do Pylint

---

## 📁 Pasta `init/`

**Propósito:** Contém scripts de inicialização do banco de dados.

### 📄 `schema.sql`

**Caminho:** `./init/schema.sql` | **Linhas:** 23  
**Propósito:** Script SQL que cria as tabelas do banco de dados e insere dados iniciais.

```sql
-- L1-L6 - Criação da tabela de pets
CREATE TABLE IF NOT EXISTS 'pets' (
  id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Chave primária auto-incrementada
  name TEXT NOT NULL,                     -- Nome do pet (obrigatório)
  type TEXT NOT NULL                      -- Tipo do pet: dog, cat, etc. (obrigatório)
);

-- L8-L15 - Criação da tabela de pessoas
CREATE TABLE IF NOT EXISTS 'people' (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,               -- Primeiro nome
  last_name TEXT NOT NULL,                -- Sobrenome
  age INTEGER NOT NULL,                   -- Idade
  pet_id INTEGER NOT NULL,                -- FK para a tabela pets
  FOREIGN KEY (pet_id) REFERENCES pets(id)  -- Relacionamento: cada pessoa TEM UM pet
);

-- L17-L23 - Dados iniciais de exemplo
INSERT INTO pets(name, type) VALUES
  ("cobra","snake"), ("cao","dog"), ("gato","cat"),
  ("jorgin","hamster"), ("burro","donkey"),
  ("shrek","ogro"), ("belinha","dog");
```

**📝 Notas Didáticas:**

- `PRIMARY KEY AUTOINCREMENT`: o banco gera IDs únicos automaticamente
- `FOREIGN KEY`: estabelece relacionamento entre tabelas (uma pessoa pertence a um pet)
- `NOT NULL`: campo obrigatório, não pode ficar vazio

---

## 📁 Pasta `src/`

**Propósito:** Diretório raiz do código-fonte. Contém toda a lógica da aplicação organizada em camadas.

**Arquivos:**

- `__init__.py` - Arquivo vazio que marca o diretório como um pacote Python

**📝 Nota:** O arquivo `__init__.py` vazio é necessário para que o Python reconheça a pasta como um módulo importável.

---

## 📁 Pasta `src/controllers/`

**Propósito:** Camada de **controle** (ou "apresentação"). Os controllers:

- Recebem dados de entrada
- Validam as informações
- Chamam os repositories para operações no banco
- Formatam a resposta de saída

**Analogia:** São como garçons - recebem o pedido do cliente, verificam se está correto, passam para a cozinha (repository) e entregam o prato pronto formatado.

---

### 📄 `person_creator_controller.py`

**Caminho:** `./src/controllers/person_creator_controller.py` | **Linhas:** 36  
**Propósito:** Controller responsável por criar novas pessoas no sistema.

**Dependências/Imports:**

```python
from typing import Dict                    # Tipagem para dicionários
import re                                  # Expressões regulares para validação
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from .interfaces.person_creator_controller import PersonCreatorControllerInterface
```

**Código completo com explicações linha-a-linha:**

```python
# L6-L9 - Definição da classe
class PersonCreatorController(PersonCreatorControllerInterface):
    # Herda da interface, OBRIGANDO a implementar o método "create"

    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        # Injeção de Dependência: recebe o repository como parâmetro
        # Isso permite trocar o repository real por um mock nos testes
        self.__people_repository = people_repository
        # O prefixo __ torna o atributo "privado" (encapsulamento)
```

```python
# L10-L19 - Método principal create()
def create(self, person_info: Dict) -> Dict:
    # L11-L14: Extrai os dados do dicionário recebido
    first_name = person_info["first_name"]
    last_name = person_info["last_name"]
    age = person_info["age"]
    pet_id = person_info["pet_id"]

    # L16: Valida se nome/sobrenome contêm apenas letras
    self.__validate_first_and_last_name(first_name, last_name)

    # L17: Insere no banco de dados via repository
    self.__insert_person_in_db(first_name, last_name, age, pet_id)

    # L18-L19: Formata e retorna a resposta padronizada
    formated_response = self.__format_response(person_info)
    return formated_response
```

```python
# L21-L28 - Validação de nome com Regex
def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
    # Regex: [^a-zA-Z] encontra qualquer caractere que NÃO seja letra
    non_valid_caracteres = re.compile(r"[^a-zA-Z]")

    # Se encontrar caractere inválido em qualquer um dos nomes...
    if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
        raise Exception("Nome da pessoa inválido")
        # Lança exceção que interrompe a execução
```

```python
# L30-L33 - Inserção no banco (delega para o repository)
def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
    self.__people_repository.insert_person(first_name, last_name, age, pet_id)
    # O controller NÃO sabe como inserir no banco - apenas chama o repository
```

```python
# L35-L36 - Formatação da resposta
def __format_response(self, person_info: Dict) -> Dict:
    return {"data": {"type": "Person", "count": 1, "attributes": person_info}}
    # Retorna um dicionário padronizado com:
    # - type: tipo do recurso
    # - count: quantidade de itens
    # - attributes: os dados em si
```

**⚠️ Possível problema:**

- A validação de nome não aceita acentos (`é`, `ã`, etc.) nem espaços. Nomes como "José" ou "Maria Clara" seriam rejeitados.

---

### 📄 `person_creator_controller_test.py`

**Caminho:** `./src/controllers/person_creator_controller_test.py` | **Linhas:** 35  
**Propósito:** Testes unitários para o `PersonCreatorController`.

```python
# L1-L3 - Imports
import pytest                                        # Framework de testes
from .person_creator_controller import PersonCreatorController


# L5-L8 - Mock do Repository
class MockPeopleRepository:
    """Objeto falso que simula o repository real"""
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass  # Não faz nada - apenas simula a assinatura do método
```

```python
# L11-L23 - Teste de sucesso
def test_create():
    # Arrange (Preparação)
    person_infor = {
        "first_name": "Fulano",
        "last_name": "deTal",
        "age": 30,
        "pet_id": 123,
    }

    # Act (Execução)
    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_infor)

    # Assert (Verificação)
    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_infor
```

```python
# L26-L35 - Teste de erro (nome inválido)
def test_create_error():
    person_infor = {
        "first_name": "Fulano123",  # Nome com números = inválido!
        "last_name": "deTal",
        "age": 30,
        "pet_id": 123,
    }

    controller = PersonCreatorController(MockPeopleRepository())

    # pytest.raises: espera que uma exceção seja lançada
    with pytest.raises(Exception):
        controller.create(person_infor)
```

**📝 Notas Didáticas:**

- **Mock**: objeto "falso" que simula comportamento real
- **Padrão AAA**: Arrange (preparar), Act (executar), Assert (verificar)
- O mock permite testar o controller SEM precisar de banco de dados real

---

### 📄 `person_finder_controller.py`

**Caminho:** `./src/controllers/person_finder_controller.py` | **Linhas:** 32  
**Propósito:** Controller responsável por buscar uma pessoa pelo ID.

```python
# L1-L4 - Imports
from typing import Dict
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import People
from .interfaces.person_finder_controller import PersonFinderControllerInterface
```

```python
# L6-L9 - Classe com injeção de dependência
class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository
```

```python
# L11-L14 - Método principal find()
def find(self, person_id: int) -> Dict:
    person = self.__find_person_in_db(person_id)  # Busca no banco
    response = self.__format_response(person)      # Formata resposta
    return response
```

```python
# L16-L20 - Busca no banco com tratamento de erro
def __find_person_in_db(self, person_id: int) -> People:
    person = self.__people_repository.get_person(person_id)
    if not person:
        raise Exception("Pessoa não encontrada!")  # Erro se não existir
    return person
```

```python
# L22-L32 - Formatação da resposta
def __format_response(self, person: People) -> Dict:
    return {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": person.first_name,
                "last_name": person.last_name,
                "pet_name": person.pet_name,    # Nome do pet (via JOIN)
                "pet_type": person.pet_type     # Tipo do pet (via JOIN)
            }
        }
    }
```

---

### 📄 `person_finder_controller_test.py`

**Caminho:** `./src/controllers/person_finder_controller_test.py` | **Linhas:** 35  
**Propósito:** Testes unitários para o `PersonFinderController`.

```python
# L1-L2 - Desabilita aviso do Pylint sobre argumentos não usados
#pylint: disable = unused-argument
from .person_finder_controller import PersonFinderController


# L5-L11 - Mock que simula uma pessoa retornada do banco
class MockPerson:
    def __init__(self, first_name, last_name, pet_name, pet_type) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type


# L14-L19 - Mock do repository
class MockPeopleRepository:
    def get_person(self, person_id: int):
        # Sempre retorna a mesma pessoa fictícia
        return MockPerson(
            first_name="John", last_name="Doe",
            pet_name="Fluffy", pet_type="cat"
        )


# L22-L35 - Teste de busca
def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(123)  # ID qualquer

    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Fluffy",
                "pet_type": "cat",
            },
        }
    }
    assert response == expected_response
```

---

### 📄 `pet_lister_controller.py`

**Caminho:** `./src/controllers/pet_lister_controller.py` | **Linhas:** 31  
**Propósito:** Controller responsável por listar todos os pets.

```python
# L1-L4 - Imports
from typing import Dict, List
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable
from .interfaces.pet_lister_controller import PetListerControllerInterface
```

```python
# L6-L9 - Classe
class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository
```

```python
# L11-L14 - Método list()
def list(self) -> Dict:
    pets = self.__get_pets_in_db()          # Busca todos os pets
    response = self.__format_response(pets)  # Formata lista
    return response
```

```python
# L16-L18 - Busca no banco
def __get_pets_in_db(self) -> List[PetsTable]:
    pets = self.__pet_repository.list_pets()
    return pets
```

```python
# L20-L31 - Formatação da lista
def __format_response(self, pets: List[PetsTable]) -> Dict:
    formatted_pets = []
    for pet in pets:
        # Extrai apenas nome e id de cada pet
        formatted_pets.append({"name": pet.name, "id": pet.id})

    return {
        "data": {
            "type": "Pets",
            "count": len(formatted_pets),  # Quantidade de pets
            "attributes": formatted_pets    # Lista de pets
        }
    }
```

---

### 📄 `pet_lister_controller_test.py`

**Caminho:** `./src/controllers/pet_lister_controller_test.py` | **Linhas:** 30  
**Propósito:** Testes unitários para o `PetListerController`.

```python
# L1-L2 - Imports
from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController


# L4-L10 - Mock que retorna lista de pets
class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="Cat", id=4),
            PetsTable(name="Buddy", type="Dog", id=47),
        ]


# L13-L30 - Teste de listagem
def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fluffy", "id": 4},
                {"name": "Buddy", "id": 47}
            ],
        }
    }
    assert response == expected_response
```

---

### 📄 `pet_deleter_controller.py`

**Caminho:** `./src/controllers/pet_deleter_controller.py` | **Linhas:** 11  
**Propósito:** Controller responsável por deletar um pet pelo nome.

```python
# L1-L3 - Imports
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pet_deleter_controller import PetDeleterControllerInterface


# L5-L10 - Classe simples de deleção
class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pet(name)
        # Delega a deleção diretamente ao repository
```

**⚠️ Possível problema:**

- O método chama `delete_pet(name)` mas a interface define `delete_pets(name)`. Pode haver inconsistência de nomes.

---

### 📄 `pet_deleter_controller_test.py`

**Caminho:** `./src/controllers/pet_deleter_controller_test.py` | **Linhas:** 10  
**Propósito:** Teste do `PetDeleterController` usando `mocker` do pytest.

```python
# L1-L9 - Teste com mocker
from src.controllers.pet_deleter_controller import PetDeleterController


def test_delete_pet(mocker):
    mock_repository = mocker.Mock()  # Cria mock dinâmico
    controller = PetDeleterController(mock_repository)
    controller.delete("amiguinho")

    # Verifica se delete_pet foi chamado UMA vez com "amiguinho"
    mock_repository.delete_pet.assert_called_once_with("amiguinho")
```

**📝 Nota:** `mocker.Mock()` cria automaticamente qualquer método chamado nele.

---

### 📄 `pets_creator_controller.py`

**Caminho:** `./src/controllers/pets_creator_controller.py` | **Linhas:** 5  
**Propósito:** Controller para criar pets (incompleto).

```python
# L1-L5 - Estrutura básica
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetsCreatorController:
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository
```

**⚠️ Possível problema:**

- Classe incompleta - não possui método `create()` nem implementa interface.

---

## 📁 Pasta `src/controllers/interfaces/`

**Propósito:** Define os **contratos** (interfaces) que os controllers devem implementar.

**Analogia:** É como um manual de instruções que diz "todo garçom DEVE saber anotar pedidos". A interface não diz COMO fazer, apenas O QUE deve ser feito.

---

### 📄 `person_creator_controller.py` (Interface)

**Caminho:** `./src/controllers/interfaces/person_creator_controller.py` | **Linhas:** 12

```python
# L1-L2 - Imports para criar interface
from typing import Dict
from abc import ABC, abstractmethod  # ABC = Abstract Base Class


# L5-L9 - Interface abstrata
class PersonCreatorControllerInterface(ABC):
    """Contrato: todo controller de criar pessoa DEVE ter método create()"""

    @abstractmethod  # Decorador que OBRIGA implementação
    def create(self, person_info: Dict) -> Dict:
        pass  # Não tem implementação - é apenas a assinatura
```

**📝 Notas Didáticas:**

- `ABC`: classe base abstrata - não pode ser instanciada diretamente
- `@abstractmethod`: marca método que DEVE ser implementado pelas classes filhas
- Se uma classe herda mas não implementa, Python lança erro

---

### 📄 `person_finder_controller.py` (Interface)

**Caminho:** `./src/controllers/interfaces/person_finder_controller.py` | **Linhas:** 12

```python
from typing import Dict
from abc import ABC, abstractmethod


class PersonFinderControllerInterface(ABC):

    @abstractmethod
    def find(self, person_id: int) -> Dict:
        pass
```

---

### 📄 `pet_lister_controller.py` (Interface)

**Caminho:** `./src/controllers/interfaces/pet_lister_controller.py` | **Linhas:** 11

```python
from typing import Dict, List
from abc import ABC, abstractmethod

class PetListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
```

**⚠️ Possível problema:**

- Import `List` não é utilizado na interface.

---

### 📄 `pet_deleter_controller.py` (Interface)

**Caminho:** `./src/controllers/interfaces/pet_deleter_controller.py` | **Linhas:** 9

```python
from abc import ABC, abstractmethod


class PetDeleterControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass
```

---

## 📁 Pasta `src/models/`

**Propósito:** Camada de **dados/modelo**. Contém tudo relacionado ao armazenamento e recuperação de dados.

---

## 📁 Pasta `src/models/sqlite/entities/`

**Propósito:** Define as **entidades** (tabelas do banco de dados) usando SQLAlchemy ORM.

**Analogia:** São os "moldes" que definem a estrutura de cada tabela. Como um formulário que diz quais campos existem.

---

### 📄 `people.py` (Entidade)

**Caminho:** `./src/models/sqlite/entities/people.py` | **Linhas:** 24

```python
# L1-L3 - Imports do SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base  # Base declarativa


# L5-L23 - Definição da tabela People
class People(Base):
    __tablename__ = "people"  # Nome da tabela no banco

    # Definição das colunas:
    id = Column(Integer, primary_key=True)       # PK auto-incrementada
    first_name = Column(String, nullable=False)  # NOT NULL
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    pet_id = Column(Integer, ForeignKey('pets.id'))  # Chave estrangeira

    # Relacionamento comentado (não ativo)
    # pets = relationship('PetsTable', back_populates='people')

    def __repr__(self):
        """Representação textual do objeto (útil para debug)"""
        return f"People(first_name={self.first_name}, last_name={self.last_name}, age={self.age})"
```

**📝 Notas Didáticas:**

- `Column`: define uma coluna da tabela
- `primary_key=True`: chave primária única
- `nullable=False`: equivalente a NOT NULL no SQL
- `ForeignKey('pets.id')`: referência à tabela pets
- `__repr__`: como o objeto aparece quando printado

---

### 📄 `pets.py` (Entidade)

**Caminho:** `./src/models/sqlite/entities/pets.py` | **Linhas:** 17

```python
# L1-L3 - Imports
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


# L5-L17 - Definição da tabela Pets
class PetsTable(Base):
    __tablename__ = "pets"  # Nome da tabela

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Nome do pet
    type = Column(String, nullable=False)  # Tipo: dog, cat, etc.

    # Relacionamento comentado
    # people = relationship('People', back_populates='pets')

    def __repr__(self):
        return f"PetsTable(name={self.name}, type={self.type})"
```

---

## 📁 Pasta `src/models/sqlite/interfaces/`

**Propósito:** Define os contratos que os repositories devem seguir.

---

### 📄 `people_repository.py` (Interface)

**Caminho:** `./src/models/sqlite/interfaces/people_repository.py` | **Linhas:** 14

```python
# L1-L3 - Imports
from abc import ABC, abstractmethod
from src.models.sqlite.entities.people import People


# L5-L14 - Interface do repository de pessoas
class PeopleRepositoryInterface(ABC):

    @abstractmethod
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        """Insere uma nova pessoa no banco"""
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> People:
        """Busca uma pessoa pelo ID"""
        pass
```

---

### 📄 `pets_repository.py` (Interface)

**Caminho:** `./src/models/sqlite/interfaces/pets_repository.py` | **Linhas:** 15

```python
# L1-L3 - Imports
from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pets import PetsTable


# L6-L15 - Interface do repository de pets
class PetsRepositoryInterface(ABC):

    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        """Lista todos os pets"""
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        """Deleta um pet pelo nome"""
        pass
```

---

## 📁 Pasta `src/models/sqlite/repositories/`

**Propósito:** Implementação concreta dos repositories. Contém a lógica real de acesso ao banco de dados.

**Analogia:** É a "cozinha" do restaurante - onde o trabalho real de preparar/buscar dados acontece.

---

### 📄 `people_repository.py` (Implementação)

**Caminho:** `./src/models/sqlite/repositories/people_repository.py` | **Linhas:** 44

```python
# L1-L4 - Imports
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import People
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
```

```python
# L6-L9 - Classe do repository
class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection  # Recebe conexão por injeção
```

```python
# L11-L23 - Inserção de pessoa
def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
    with self.__db_connection as database:
        # "with" garante que a conexão será fechada ao final
        try:
            person_data = People(
                first_name=first_name,
                last_name=last_name,
                age=age,
                pet_id=pet_id
            )
            database.session.add(person_data)   # Adiciona à sessão
            database.session.commit()           # Salva no banco
        except Exception as exception:
            database.session.rollback()         # Desfaz em caso de erro
            raise exception
```

```python
# L25-L44 - Busca de pessoa com JOIN
def get_person(self, person_id: int) -> People:
    with self.__db_connection as database:
        try:
            person = (
                database.session
                    .query(People)
                    .outerjoin(PetsTable, PetsTable.id == People.id)  # LEFT JOIN
                    .filter(People.id == person_id)
                    .with_entities(                    # Seleciona campos específicos
                        People.first_name,
                        People.last_name,
                        PetsTable.name.label("pet_name"),   # Alias
                        PetsTable.type.label("pet_type"),
                    )
                    .one()                             # Retorna exatamente 1 resultado
            )
            return person
        except NoResultFound:
            return None  # Retorna None se não encontrar
```

**⚠️ Possível problema:**

- O JOIN usa `PetsTable.id == People.id` mas deveria ser `PetsTable.id == People.pet_id`.

---

### 📄 `pets_repository.py` (Implementação)

**Caminho:** `./src/models/sqlite/repositories/pets_repository.py` | **Linhas:** 33

```python
# L1-L5 - Imports
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
```

```python
# L7-L10 - Classe
class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
```

```python
# L12-L19 - Listagem de pets
def list_pets(self) -> List[PetsTable]:
    with self.__db_connection as database:
        try:
            pets = database.session.query(PetsTable).all()  # SELECT * FROM pets
            return pets
        except NoResultFound:
            return []  # Lista vazia se não houver pets
```

```python
# L21-L33 - Deleção de pet
def delete_pets(self, name: str) -> None:
    with self.__db_connection as database:
        try:
            (
                database.session
                .query(PetsTable)
                .filter(PetsTable.name == name)  # WHERE name = ?
                .delete()                         # DELETE
            )
            database.session.commit()
        except Exception as exception:
            database.session.rollback()
            raise exception
```

---

### 📄 `pets_repository_test.py`

**Caminho:** `./src/models/sqlite/repositories/pets_repository_test.py` | **Linhas:** 80  
**Propósito:** Testes unitários do `PetsRepository` usando `mock_alchemy`.

```python
# L1-L6 - Imports
from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock  # Mock especial para SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository
```

```python
# L9-L25 - Mock de conexão com dados predefinidos
class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],  # Quando chamar query(PetsTable)...
                    [                               # ...retornar esses dados
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],
                )
            ]
        )

    def __enter__(self):    # Para funcionar com "with"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

```python
# L28-L41 - Mock que simula erro
class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

```python
# L44-L54 - Teste de listagem
def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    # Verifica se os métodos corretos foram chamados
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"
```

---

### 📄 `repositories_test.py`

**Caminho:** `./src/models/sqlite/repositories/repositories_test.py` | **Linhas:** 38  
**Propósito:** Testes de **integração** com banco real (marcados como skip).

```python
# L1-L5 - Imports
import pytest
from src.models.sqlite.settings.connection import db_connecition_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository
```

```python
# L9-L12 - Teste de listagem (skip por padrão)
@pytest.mark.skip(reason="interacao com o banco")  # Pula nos testes normais
def test_list_pets():
    repo = PetsRepository(db_connecition_handler)
    response = repo.list_pets()
    print(response)
```

**📝 Nota:** Estes testes são "skipped" por padrão pois dependem de banco real. Remova o decorador para executar manualmente.

---

## 📁 Pasta `src/models/sqlite/settings/`

**Propósito:** Configurações de conexão e base do SQLAlchemy.

---

### 📄 `base.py`

**Caminho:** `./src/models/sqlite/settings/base.py` | **Linhas:** 5

```python
# L1-L4 - Criação da Base declarativa
# from sqlalchemy.ext.declarative import declarative_base (old)  # Forma antiga
from sqlalchemy.orm import declarative_base  # Forma nova (SQLAlchemy 2.0)

Base = declarative_base()
# Base é a classe-mãe de todas as entidades
# Permite que o SQLAlchemy rastreie as tabelas automaticamente
```

---

### 📄 `connection.py`

**Caminho:** `./src/models/sqlite/settings/connection.py` | **Linhas:** 26

```python
# L1-L2 - Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# L5-L26 - Classe de conexão
class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"  # Arquivo SQLite
        self.__engine = None      # Motor de conexão
        self.session = None       # Sessão atual

    def connect_to_db(self):
        """Cria o motor de conexão com o banco"""
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        """Retorna o motor de conexão"""
        return self.__engine

    def __enter__(self):
        """Chamado ao entrar no "with" - cria sessão"""
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Chamado ao sair do "with" - fecha sessão"""
        self.session.close()


# Instância global (singleton)
db_connecition_handler = DBConnectionHandler()
```

**📝 Notas Didáticas:**

- **Context Manager** (`__enter__`/`__exit__`): permite usar `with db_connection as db:`
- **Singleton**: `db_connecition_handler` é uma única instância compartilhada
- O arquivo do banco (`storage.db`) é criado na raiz do projeto

**⚠️ Possível problema:**

- Typo no nome: `db_connecition_handler` deveria ser `db_connection_handler`.

---

### 📄 `connection_test.py`

**Caminho:** `./src/models/sqlite/settings/connection_test.py` | **Linhas:** 13

```python
# L1-L3 - Imports
import pytest
from sqlalchemy.engine import Engine
from .connection import db_connecition_handler


# L7-L13 - Teste de conexão
def test_connect_to_db():
    # Antes de conectar, engine deve ser None
    assert db_connecition_handler.get_engine() is None

    db_connecition_handler.connect_to_db()
    db_engine = db_connecition_handler.get_engine()

    # Após conectar, deve ser uma instância de Engine
    assert db_engine is not None
    assert isinstance(db_engine, Engine)
```

---

## 🚀 Comandos Úteis

### Instalação do Ambiente

```powershell
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# 3. Instalar dependências
pip install -r requirements.txt
```

### Executar Testes

```powershell
# Rodar todos os testes
pytest

# Rodar com detalhes
pytest -s -v

# Rodar arquivo específico
pytest src/controllers/person_creator_controller_test.py -v

# Rodar teste específico
pytest -k "test_create" -v
```

### Criar Banco de Dados

```powershell
# Via SQLite CLI
sqlite3 storage.db < init/schema.sql
```

### Verificar Código com Pylint

```powershell
pylint src/
```

### Executar Módulo

```powershell
# Executar como módulo (recomendado)
python -m src.models.sqlite.repositories.pets_repository
```

---

## ✅ Checklist de Entendimento

Após ler esta documentação, o estagiário deve ser capaz de responder:

- [ ] O que é o padrão Repository e por que ele é usado?
- [ ] Qual a diferença entre uma Interface (ABC) e uma Implementação?
- [ ] O que é Injeção de Dependência e por que é útil para testes?
- [ ] Como o SQLAlchemy mapeia classes Python para tabelas SQL?
- [ ] O que é um Context Manager (`with`) e como funciona?
- [ ] Por que usamos Mocks nos testes unitários?
- [ ] Como a estrutura de pastas separa responsabilidades?
- [ ] O que acontece quando um método `@abstractmethod` não é implementado?

---

## ❓ Perguntas Sugeridas

Perguntas que um estagiário pode fazer para aprofundar o entendimento:

1. **"Como adiciono uma nova entidade (tabela) ao projeto?"**
2. **"Como faço para rodar apenas os testes de integração com banco real?"**
3. **"Por que os relacionamentos entre People e Pets estão comentados?"**
4. **"Como funcionaria se eu quisesse trocar SQLite por PostgreSQL?"**
5. **"O que é o `UnifiedAlchemyMagicMock` e por que não usar `Mock()` normal?"**
6. **"Como adiciono validação de idade mínima no `PersonCreatorController`?"**

---

## 📜 Histórico de Geração

| Versão | Data       | Observações                                        |
| ------ | ---------- | -------------------------------------------------- |
| 1.0    | 2025-11-27 | Versão inicial                                     |
| 2.0    | 2025-12-02 | Atualização completa com explicações linha-a-linha |

---

**📝 Observações Finais:**

1. **Typo identificado:** `db_connecition_handler` → deveria ser `db_connection_handler`
2. **Código incompleto:** `PetsCreatorController` não possui implementação
3. **JOIN incorreto:** Em `people_repository.py`, o JOIN usa `PetsTable.id == People.id` mas deveria ser `PetsTable.id == People.pet_id`
4. **Validação limitada:** Validação de nome não suporta acentos ou espaços
5. **Imports não utilizados:** `List` importado mas não usado em algumas interfaces

---

_Documento gerado automaticamente por GitHub Copilot - Agent AI_
