import enum
from   datetime     import datetime, timezone
from   sqlalchemy   import Column, Integer, String, DateTime, Enum, ForeignKey
from   app.database import Base


class TipoExameEnum(str, enum.Enum):
    HEMOGRAMA = "Hemograma"    
    RAIO_X    = "Raio-X"
    ECG       = "ECG"


class StatusExameEnum(str, enum.Enum):
    SOLICITADO = "Solicitado"
    CONCLUIDO  = "Concluído"


class Exame(Base):
    __tablename__ = "exames"

    id             = Column (Integer, primary_key=True, index=True)
    atendimento_id = Column (Integer, ForeignKey("atendimentos.id"), nullable=False)
    tipo_exame     = Column (Enum(TipoExameEnum), nullable=False)
    resultado      = Column (String, nullable=True)
    status         = Column (Enum(StatusExameEnum), default=StatusExameEnum.SOLICITADO, nullable=False)
    data_hora      = Column (DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)