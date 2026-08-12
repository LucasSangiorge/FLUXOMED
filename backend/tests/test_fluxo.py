def criar_paciente(client, cpf):
    resposta = client.post("/pacientes/", json={
        "nome": "Paciente Teste",
        "data_nascimento": "1990-01-01",
        "cpf": cpf,
        "telefone": "31999999999",
        "convenio": "Unimed",
        "numero_carteirinha": "123",
    })
    assert resposta.status_code == 200
    return resposta.json()


def criar_atendimento(client, paciente_id, senha):
    resposta = client.post("/atendimentos/", json={
        "paciente_id": paciente_id,
        "senha": senha,
    })
    assert resposta.status_code == 200
    return resposta.json()


def test_fluxo_completo_ate_alta(client):
    paciente = criar_paciente(client, "11111111111")
    atendimento = criar_atendimento(client, paciente["id"], "A001")

    resposta_triagem = client.post("/triagens/", json={
        "atendimento_id": atendimento["id"],
        "sintomas": "Dor de cabeça",
        "pressao_arterial": "120/80",
        "cor_classificacao": "Amarelo",
    })
    assert resposta_triagem.status_code == 200

    resposta_consulta = client.post("/consultas/", json={
        "atendimento_id": atendimento["id"],
        "descricao_medico": "Paciente estável, liberado",
    })
    assert resposta_consulta.status_code == 200

    resposta_alta = client.post("/altas/", json={
        "atendimento_id": atendimento["id"],
        "observacoes": "Sem intercorrências",
    })
    assert resposta_alta.status_code == 200


def test_alta_bloqueada_sem_consulta(client):
    paciente = criar_paciente(client, "22222222222")
    atendimento = criar_atendimento(client, paciente["id"], "A002")

    resposta_alta = client.post("/altas/", json={"atendimento_id": atendimento["id"]})
    assert resposta_alta.status_code == 400


def test_fila_espera_ordena_por_risco(client):
    paciente = criar_paciente(client, "33333333333")

    atendimento_amarelo = criar_atendimento(client, paciente["id"], "A003")
    client.post("/triagens/", json={
        "atendimento_id": atendimento_amarelo["id"],
        "sintomas": "Dor leve",
        "pressao_arterial": "110/70",
        "cor_classificacao": "Amarelo",
    })

    atendimento_vermelho = criar_atendimento(client, paciente["id"], "A004")
    client.post("/triagens/", json={
        "atendimento_id": atendimento_vermelho["id"],
        "sintomas": "Falta de ar",
        "pressao_arterial": "90/60",
        "cor_classificacao": "Vermelho",
    })

    resposta_fila = client.get("/fila-espera/")
    assert resposta_fila.status_code == 200
    fila = resposta_fila.json()

    assert len(fila) == 2
    assert fila[0]["atendimento_id"] == atendimento_vermelho["id"]
    assert fila[1]["atendimento_id"] == atendimento_amarelo["id"]
