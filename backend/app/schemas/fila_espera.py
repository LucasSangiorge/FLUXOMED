from datetime import datetime
from pydantic import BaseModel
from app.models.triagem import CorClassificacaoEnum


class FilaEsperaResponse(BaseModel):
    atendimento_id    : int
    paciente_id       : int
    senha             : str
    cor_classificacao : CorClassificacaoEnum
    data_hora_chegada : datetime

    class Config:
        from_attributes = True
