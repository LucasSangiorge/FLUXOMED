const API_URL = "http://127.0.0.1:8000";

function mostrarMensagem(elementoId, texto, tipo) {
  const elemento = document.getElementById(elementoId);
  elemento.textContent = texto;
  elemento.className = "msg " + tipo;
}

async function enviarFormulario(url, dados, msgId, form) {
  try {
    const resposta = await fetch(API_URL + url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados),
    });

    if (!resposta.ok) {
      const erro = await resposta.json();
      mostrarMensagem(msgId, "Erro: " + JSON.stringify(erro.detail), "erro");
      return;
    }

    const resultado = await resposta.json();
    mostrarMensagem(msgId, "Sucesso! ID gerado: " + resultado.id, "ok");
    form.reset();
  } catch (erro) {
    mostrarMensagem(msgId, "Erro de conexão com a API", "erro");
  }
}

document.getElementById("form-paciente").addEventListener("submit", function (evento) {
  evento.preventDefault();
  const dados = {
    nome: document.getElementById("paciente-nome").value,
    data_nascimento: document.getElementById("paciente-nascimento").value,
    cpf: document.getElementById("paciente-cpf").value,
    telefone: document.getElementById("paciente-telefone").value,
    convenio: document.getElementById("paciente-convenio").value,
    numero_carteirinha: document.getElementById("paciente-carteirinha").value,
  };
  enviarFormulario("/pacientes/", dados, "msg-paciente", evento.target);
});

document.getElementById("form-atendimento").addEventListener("submit", function (evento) {
  evento.preventDefault();
  const dados = {
    paciente_id: Number(document.getElementById("atendimento-paciente-id").value),
    senha: document.getElementById("atendimento-senha").value,
  };
  enviarFormulario("/atendimentos/", dados, "msg-atendimento", evento.target);
});

document.getElementById("form-triagem").addEventListener("submit", function (evento) {
  evento.preventDefault();
  const dados = {
    atendimento_id: Number(document.getElementById("triagem-atendimento-id").value),
    sintomas: document.getElementById("triagem-sintomas").value,
    pressao_arterial: document.getElementById("triagem-pressao").value,
    cor_classificacao: document.getElementById("triagem-cor").value,
  };
  enviarFormulario("/triagens/", dados, "msg-triagem", evento.target);
});

document.getElementById("form-consulta").addEventListener("submit", function (evento) {
  evento.preventDefault();
  const dados = {
    atendimento_id: Number(document.getElementById("consulta-atendimento-id").value),
    descricao_medico: document.getElementById("consulta-descricao").value,
  };
  enviarFormulario("/consultas/", dados, "msg-consulta", evento.target);
});

document.getElementById("form-exame").addEventListener("submit", function (evento) {
  evento.preventDefault();
  const dados = {
    atendimento_id: Number(document.getElementById("exame-atendimento-id").value),
    tipo_exame: document.getElementById("exame-tipo").value,
    resultado: document.getElementById("exame-resultado").value || null,
  };
  enviarFormulario("/exame/", dados, "msg-exame", evento.target);
});

document.getElementById("form-medicamento").addEventListener("submit", function (evento) {
  evento.preventDefault();
  const dados = {
    atendimento_id: Number(document.getElementById("medicamento-atendimento-id").value),
    nome_medicacao: document.getElementById("medicamento-nome").value,
    dosagem: document.getElementById("medicamento-dosagem").value,
  };
  enviarFormulario("/medicamentos/", dados, "msg-medicamento", evento.target);
});

document.getElementById("form-alta").addEventListener("submit", function (evento) {
  evento.preventDefault();
  const dados = {
    atendimento_id: Number(document.getElementById("alta-atendimento-id").value),
    observacoes: document.getElementById("alta-observacoes").value || null,
  };
  enviarFormulario("/altas/", dados, "msg-alta", evento.target);
});

async function atualizarFila() {
  const corpoTabela = document.getElementById("corpo-fila");
  corpoTabela.innerHTML = "";

  try {
    const resposta = await fetch(API_URL + "/fila-espera/");
    const fila = await resposta.json();

    fila.forEach(function (item) {
      const linha = document.createElement("tr");
      linha.innerHTML =
        "<td>" + item.atendimento_id + "</td>" +
        "<td>" + item.paciente_id + "</td>" +
        "<td>" + item.senha + "</td>" +
        "<td>" + item.cor_classificacao + "</td>" +
        "<td>" + new Date(item.data_hora_chegada).toLocaleString() + "</td>";
      corpoTabela.appendChild(linha);
    });
  } catch (erro) {
    corpoTabela.innerHTML = "<tr><td colspan='5'>Erro ao carregar a fila</td></tr>";
  }
}

document.getElementById("btn-fila").addEventListener("click", atualizarFila);
