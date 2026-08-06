from datetime             import datetime
from pydantic             import BaseModel
from app.models.medicacao import TipoMedicamentoEnum

class MedicamentoBase(BaseModel):
    atendimento_id      : int
    nome_medicacao      : TipoMedicamentoEnum
    dosagem             : str

class MedicamentoCreate(MedicamentoBase):
    pass 

class MedicamentoResponse(MedicamentoBase):
    id        : int
    data_hora : datetime

    class Config:
        from_attributes = True