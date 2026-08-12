from fastapi                 import APIRouter, Depends
from sqlalchemy.orm          import Session
from app.database             import get_db
from app.models.atendimento  import Atendimento, StatusAtendimentoEnum
from app.models.triagem      import Triagem, CorClassificacaoEnum
from app.models.consulta     import Consulta
from app.schemas.fila_espera import FilaEsperaResponse

router = APIRouter(prefix="/fila-espera", tags=["Fila de Espera"])

ORDEM_RISCO = {
    CorClassificacaoEnum.VERMELHO: 1,
    CorClassificacaoEnum.LARANJA: 2,
    CorClassificacaoEnum.AMARELO: 3,
}

@router.get("/", response_model=list[FilaEsperaResponse])
def listar_fila_espera(db: Session = Depends(get_db)):
    consultados_ids = [c.atendimento_id for c in db.query(Consulta).all()]

    resultados = (
        db.query(Atendimento, Triagem)
        .join(Triagem, Triagem.atendimento_id == Atendimento.id)
        .filter(Atendimento.status == StatusAtendimentoEnum.EM_ANDAMENTO)
        .filter(~Atendimento.id.in_(consultados_ids))
        .all()
    )

    fila = [
        FilaEsperaResponse(
            atendimento_id=atendimento.id,
            paciente_id=atendimento.paciente_id,
            senha=atendimento.senha,
            cor_classificacao=triagem.cor_classificacao,
            data_hora_chegada=atendimento.data_hora_chegada,
        )
        for atendimento, triagem in resultados
    ]

    fila.sort(key=lambda item: (ORDEM_RISCO[item.cor_classificacao], item.data_hora_chegada))

    return fila
