from datetime import datetime
from pydantic import BaseModel

class ConsultaBase(BaseModel):
    atendimento_id   : int
    descricao_medico : str

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaResponse(ConsultaBase):
    id        : int
    data_hora : datetime

    class Config:
        from_attributes = True