from datetime               import datetime
from pydantic               import BaseModel
from app.models.atendimento import StatusAtendimentoEnum

class AtendimentoBase(BaseModel):
    paciente_id : int
    senha       : str


class AtendimentoCreate(AtendimentoBase):
    pass

class AtendimentoResponse(AtendimentoBase):
    id                : int
    data_hora_chegada : datetime
    status            : StatusAtendimentoEnum

    class Config:
        from_attributes = True