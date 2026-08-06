from datetime import datetime
from pydantic import BaseModel
from typing   import Optional


class AltaBase(BaseModel):
    atendimento_id : int
    observacoes : Optional[str] = None

class AltaCreate(AltaBase):
    pass

class AltaResponse(AltaBase):
    id        : int
    data_hora : datetime

    class Config:
        from_attributes = True
        