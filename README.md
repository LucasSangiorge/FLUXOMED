# FluxoMed

Projeto de portfólio backend simulando o fluxo de atendimento de um Pronto Socorro, do cadastro do paciente até a alta hospitalar.

Fluxo do domínio: Chegada → Recepção → Cadastro → Triagem → Classificação de Risco → Fila de Espera → Consulta Médica → Exames → Medicação → Alta Hospitalar.

## Stack

- **Backend:** Python + FastAPI + SQLAlchemy + Alembic
- **Banco de dados:** PostgreSQL (hospedado no Neon)
- **Frontend:** HTML + CSS + JavaScript puro (sem framework), consumindo a API via fetch
- **Testes:** Pytest + TestClient do FastAPI

## Como rodar o backend

```bash
cd backend
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash)
pip install -r requirements.txt
```

Crie um arquivo `.env` na pasta `backend/` a partir do `.env.example`, com a URL de conexão do seu banco PostgreSQL.

```bash
uvicorn app.main:app --reload
```

A API sobe em `http://127.0.0.1:8000`. Documentação interativa (Swagger) em `http://127.0.0.1:8000/docs`.

## Como rodar o frontend

Abra `frontend/index.html` direto no navegador (ou use a extensão Live Server do VSCode), com o backend rodando em paralelo.

## Como rodar os testes

```bash
cd backend
python -m pytest tests/ -v
```

## Estrutura do projeto

```
backend/
  app/
    models/      # Tabelas (SQLAlchemy)
    schemas/     # Validação de entrada/saída (Pydantic)
    routers/     # Endpoints da API
    services/    # Regras de negócio
    database.py  # Conexão com o banco
    main.py      # Aplicação FastAPI
  tests/         # Testes automatizados
frontend/
  index.html
  style.css
  script.js
doc/
  ROADMAP.md     # Progresso detalhado do projeto
```

## Regras de negócio implementadas

- A fila de espera é ordenada automaticamente por classificação de risco (Vermelho → Laranja → Amarelo) e, dentro da mesma cor, por ordem de chegada.
- Não é possível dar alta a um atendimento que ainda não passou por consulta médica.

## Progresso

O andamento detalhado por fase está em [`doc/ROADMAP.md`](doc/ROADMAP.md).
