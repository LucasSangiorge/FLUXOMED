from sqlalchemy.orm         import Session
from fastapi                import HTTPException
from app.models.consulta    import Consulta
from app.models.atendimento import Atendimento, StatusAtendimentoEnum


def validar_alta(atendimento_id: int, db: Session):
    consulta = db.query(Consulta).filter(Consulta.atendimento_id == atendimento_id).first()
    if not consulta:
        raise HTTPException(
            status_code=400,
            detail="Não é possível dar alta: atendimento ainda não passou por consulta médica",
        )

    atendimento = db.query(Atendimento).filter(Atendimento.id == atendimento_id).first()
    if not atendimento:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")
    if atendimento.status == StatusAtendimentoEnum.CONCLUIDO:
        raise HTTPException(status_code=400, detail="Atendimento já foi encerrado")

    return atendimento
