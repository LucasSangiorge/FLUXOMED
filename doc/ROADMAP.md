# ROADMAP — FluxoMed

Sistema de fluxo de Pronto Socorro (backend), construído como projeto de portfólio.

Fluxo do domínio: Chegada → Recepção → Cadastro → Triagem → Classificação de Risco → Fila de Espera → Consulta Médica → Exames → Medicação → Alta Hospitalar.

## Fase 0 — Ambiente e organização
- [x] Estrutura de pastas do projeto
- [x] Ambiente virtual (venv)
- [x] Git iniciado + `.gitignore`
- [x] Repositório criado no GitHub
- [x] Primeiro push (estrutura inicial)

## Fase 1 — Base do backend
- [x] Instalar FastAPI, Uvicorn, SQLAlchemy, Alembic, driver PostgreSQL
- [x] `requirements.txt` preenchido
- [x] Banco PostgreSQL criado no Neon (usado desde o desenvolvimento, não só no deploy)
- [x] `.env.example` (modelo de variáveis, vai pro GitHub)
- [x] `.env` com credenciais reais do Neon (fora do git)
- [x] `app/main.py` — aplicação FastAPI rodando ("Hello World")
- [x] `app/database.py` — conexão com o Neon

## Fase 2 — Modelagem do banco de dados
- [x] Model: Paciente (cadastro, com convênio fixo: Unimed, Bradesco Saúde, SulAmérica)
- [x] Model: Atendimento (representa a "Chegada" + senha/token, liga tudo)
- [x] Model: Triagem (sintomas, pressão arterial e cor de classificação de risco: Amarelo/Laranja/Vermelho — já inclui a classificação de risco, sem tabela separada)
- [x] Model: Consulta
- [x] Model: Exame (tipo fixo: Hemograma, Raio-X, ECG)
- [x] Model: Medicamento (tipo fixo: Dipirona, Paracetamol, Ondansetrona, Buscopan)
- [x] Model: Alta
- [x] Migrations com Alembic (histórico versionado do banco)

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
- [ ] Deploy da API (Render, plano free)
- [ ] Testar API publicada

## Fase 8 — Portfólio
- [ ] Repositório GitHub organizado e documentado
- [ ] Posts no LinkedIn contando o processo
