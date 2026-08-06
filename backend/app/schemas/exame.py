from datetime         import datetime
from pydantic         import BaseModel
from typing           import Optional
from app.models.exame import StatusExameEnum, TipoExameEnum

class ExameBase(BaseModel):
    atendimento_id : int
    tipo_exame     : TipoExameEnum
    resultado      : Optional[str] = None

class ExameCreate(ExameBase):
    pass

class ExameResponse(ExameBase):
    status    : StatusExameEnum
    data_hora : datetime
    id        : int

    class Config:
        from_attributes = True