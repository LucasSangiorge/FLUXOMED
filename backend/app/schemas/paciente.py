from datetime import date
from pydantic import BaseModel
from app.models.paciente import ConvenioEnum

class PacienteBase(BaseModel):
    nome               : str
    data_nascimento    : date
    cpf                : str
    telefone           : str
    convenio           : ConvenioEnum
    numero_carteirinha : str

class PacienteCreate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id: int

    class Config:
        from_attributes = True