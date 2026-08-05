import  enum
from    datetime     import datetime, timezone
from    sqlalchemy   import Column, Integer, DateTime, Enum, ForeignKey, String
from    app.database import Base

class StatusAtendimentoEnum(str, enum.Enum):
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDO    = "Concluído"
    ARQUIVADO    = "Arquivado"

class Atendimento(Base):
    __tablename__="atendimentos"

    id                = Column (Integer, primary_key=True, index=True)
    paciente_id       = Column (Integer, ForeignKey("pacientes.id"), nullable=False)
    senha             = Column (String, nullable=False)
    data_hora_chegada = Column (DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    status            = Column (Enum(StatusAtendimentoEnum), default=StatusAtendimentoEnum.EM_ANDAMENTO, nullable=False)
