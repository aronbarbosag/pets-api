# 🐾 API de Gerenciamento de Pets e Pessoas

API REST em Flask para gerenciamento de pets e pessoas.

---

# 🐾 API de Gerenciamento de Pets e Pessoas

API REST em Flask para gerenciamento de pets e pessoas.

---

## 🚀 Como Rodar

### Opção 1: Usando UV (Recomendado) ⚡

```bash
# Instalar UV (caso não tenha)
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux/Mac
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sincronizar dependências (cria .venv automaticamente)
uv sync

# Rodar o servidor
uv run python run.py

# Rodar testes
uv run pytest -s -v

# Verificar código com Ruff
uv run ruff check src/
```

### Opção 2: Usando venv tradicional

```powershell
# Criar ambiente
python -m venv venv

# Ativar (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor
python run.py
```

### 🛠️ Comandos Úteis com UV

```bash
# Adicionar nova dependência
uv add <package-name>

# Adicionar dependência de desenvolvimento
uv add --dev <package-name>

# Remover dependência
uv remove <package-name>

# Atualizar todas as dependências
uv sync --upgrade

# Rodar script Python
uv run python script.py

# Rodar testes
uv run pytest

# Formatar código
uv run ruff format src/

# Verificar código
uv run ruff check src/

# Executar pre-commit manualmente
uv run pre-commit run --all-files
```

O servidor iniciará em: `http://localhost:3000`

---

## 📡 Rotas da API

### 🐶 Pets

| Método   | Rota           | Descrição               |
| -------- | -------------- | ----------------------- |
| `GET`    | `/pets`        | Lista todos os pets     |
| `DELETE` | `/pets/<name>` | Deleta um pet pelo nome |

### 👤 Pessoas

| Método | Rota                  | Descrição            |
| ------ | --------------------- | -------------------- |
| `POST` | `/people`             | Cria uma nova pessoa |
| `GET`  | `/people/<person_id>` | Busca pessoa pelo ID |

---

## 📬 Exemplos no Postman

### 1. Listar Pets

```
GET http://localhost:3000/pets
```

**Resposta:**

```json
{
  "data": {
    "type": "Pets",
    "count": 3,
    "attributes": [
      { "name": "cao", "id": 1 },
      { "name": "gato", "id": 2 }
    ]
  }
}
```

---

### 2. Deletar Pet

```
DELETE http://localhost:3000/pets/cao
```

**Resposta:**

```json
{
  "data": {
    "type": "Pet",
    "count": 1,
    "attributes": { "name": "cao" }
  }
}
```

---

### 3. Criar Pessoa

```
POST http://localhost:3000/people
Content-Type: application/json
```

**Body (JSON):**

```json
{
  "first_name": "Fulano",
  "last_name": "Silva",
  "age": 25,
  "pet_id": 1
}
```

**Resposta:**

```json
{
  "data": {
    "type": "Person",
    "count": 1,
    "attributes": {
      "first_name": "Fulano",
      "last_name": "Silva",
      "age": 25,
      "pet_id": 1
    }
  }
}
```

> ⚠️ **Atenção:** `first_name` e `last_name` devem conter apenas letras (sem números, acentos ou espaços).

---

### 4. Buscar Pessoa por ID

```
GET http://localhost:3000/people/1
```

**Resposta:**

```json
{
  "data": {
    "type": "Person",
    "count": 1,
    "attributes": {
      "first_name": "Fulano",
      "last_name": "Silva",
      "pet_name": "cao",
      "pet_type": "dog"
    }
  }
}
```

---

## 🧪 Rodar Testes

```bash
# Todos os testes
pytest -s -v

# Apenas testes unitários (sem banco)
pytest -s -v -k "not skip"
```

---

## 📁 Estrutura do Projeto

```
├── run.py                 # Ponto de entrada
├── requirements.txt       # Dependências
├── storage.db             # Banco SQLite
├── init/
│   └── schema.sql         # Script de criação do banco
└── src/
    ├── controllers/       # Lógica de negócio
    ├── models/            # Entidades e repositories
    ├── views/             # Camada HTTP
    └── main/
        ├── routes/        # Rotas Flask
        ├── composer/      # Injeção de dependência
        └── server/        # Configuração do Flask
```

---

## 🛠️ Tecnologias

- Python 3.12
- Flask
- SQLAlchemy
- SQLite
- Pytest
