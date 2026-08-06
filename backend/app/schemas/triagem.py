from datetime import datetime
from pydantic import BaseModel
from app.models.triagem import CorClassificacaoEnum

class TriagemBase(BaseModel):
    atendimento_id    : int
    sintomas          : str
    pressao_arterial  : str
    cor_classificacao : CorClassificacaoEnum
    

class TriagemCreate(TriagemBase):
    pass

class TriagemResponse(TriagemBase):
    id        : int
    data_hora : datetime

    class Config :
        from_attributes = True