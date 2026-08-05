import enum
from   sqlalchemy   import Column, Integer, String, DateTime, Enum, ForeignKey
from   datetime     import datetime, timezone
from   app.database import Base

class TipoMedicamentoEnum(str, enum.Enum):
    DIPIRONA     = "Dipirona"
    PARACETAMOL  = "Paracetamol"
    BUSCOPAN     = "Buscopan"
    ONDANSETRONA = "Ondansetrona"

class Medicamento (Base):
    __tablename__ = "medicamentos"

    id             = Column (Integer, primary_key=True, index=True)
    atendimento_id = Column (Integer, ForeignKey("atendimentos.id"), nullable=False)
    data_hora      = Column (DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    nome_medicacao = Column (Enum(TipoMedicamentoEnum), nullable=False)
    dosagem        = Column (String, nullable=False)