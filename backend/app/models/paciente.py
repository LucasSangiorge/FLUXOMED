import enum
from   sqlalchemy     import Column, Integer, String, Date, Enum
from   app.database   import Base

class ConvenioEnum(str, enum.Enum):
    UNIMED          = "Unimed"
    BRADESCO_SAUDE  = "Bradesco Saúde"
    SULAMERICA      = "SulAmérica"

class Paciente(Base):
    __tablename__="pacientes"

    id                 = Column (Integer, primary_key=True, index=True)
    nome               = Column (String, nullable=False)
    data_nascimento    = Column (Date, nullable=False)
    cpf                = Column (String, unique=True, nullable=False)
    telefone           = Column (String, nullable= False)
    convenio          = Column  (Enum(ConvenioEnum), nullable=False)
    numero_carteirinha = Column (String, nullable=False)
    