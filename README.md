# 🐾 API de Gerenciamento de Pets e Pessoas

API REST em Flask para gerenciamento de pets e pessoas.

---

## 🚀 Como Rodar

### 1. Criar e ativar ambiente virtual

```powershell
# Criar ambiente
python -m venv venv

# Ativar (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar (Linux/Mac)
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Criar banco de dados

```bash
sqlite3 storage.db < init/schema.sql
```

### 4. Rodar o servidor

```bash
python run.py
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
