# ROADMAP — FluxoMed

Sistema de fluxo de Pronto Socorro (backend), construído como projeto de portfólio.

Fluxo do domínio: Chegada → Recepção → Cadastro → Triagem → Classificação de Risco → Fila de Espera → Consulta Médica → Exames → Medicação → Alta Hospitalar.

## Fase 0 — Ambiente e organização
- [x] Estrutura de pastas do projeto
- [x] Ambiente virtual (venv)
- [x] Git iniciado + `.gitignore`
- [ ] Repositório criado no GitHub
- [ ] Primeiro push (estrutura inicial)

## Fase 1 — Base do backend
- [ ] Instalar FastAPI, Uvicorn, SQLAlchemy, Alembic, driver PostgreSQL
- [ ] `requirements.txt` preenchido
- [ ] `app/main.py` — aplicação FastAPI rodando ("Hello World")
- [ ] `app/database.py` — conexão com PostgreSQL
- [ ] `.env` com credenciais do banco (fora do git)

## Fase 2 — Modelagem do banco de dados
- [ ] Model: Paciente (cadastro)
- [ ] Model: Atendimento (representa a "Chegada", liga tudo)
- [ ] Model: Triagem
- [ ] Model: ClassificacaoRisco
- [ ] Model: Consulta
- [ ] Model: Exame
- [ ] Model: Medicacao
- [ ] Model: Alta
- [ ] Migrations com Alembic (histórico versionado do banco)

## Fase 3 — Schemas (Pydantic)
- [ ] Schema de entrada/saída para cada entidade acima

## Fase 4 — Endpoints (routers), um por etapa do fluxo
- [ ] Recepção / Chegada — registrar entrada do paciente
- [ ] Cadastro — criar/consultar paciente
- [ ] Triagem — registrar sinais vitais, sintomas
- [ ] Classificação de Risco — definir cor/prioridade (protocolo Manchester simplificado)
- [ ] Fila de Espera — listar pacientes aguardando, ordenados por risco
- [ ] Consulta Médica — registrar atendimento médico
- [ ] Exames — solicitar/registrar resultado
- [ ] Medicação — registrar medicação aplicada
- [ ] Alta Hospitalar — encerrar o atendimento

## Fase 5 — Regras de negócio (services)
- [ ] Ordenação automática da fila por classificação de risco
- [ ] Validações de transição de status (ex: não pode dar alta sem consulta)

## Fase 6 — Qualidade
- [ ] Testes básicos dos principais endpoints
- [ ] Documentação automática (Swagger, já vem com FastAPI)
- [ ] README do projeto (o que é, como rodar, prints da documentação)

## Fase 7 — Deploy gratuito
- [ ] Banco PostgreSQL na nuvem (Neon ou Supabase, plano free)
- [ ] Deploy da API (Render, plano free)
- [ ] Testar API publicada

## Fase 8 — Portfólio
- [ ] Repositório GitHub organizado e documentado
- [ ] Posts no LinkedIn contando o processo
