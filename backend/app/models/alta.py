from   sqlalchemy   import Column, Integer, String, DateTime, Enum, ForeignKey
from   datetime     import datetime, timezone
from   app.database import Base

class Alta (Base):
    __tablename__ = "altas"

    id             = Column (Integer, primary_key=True, index=True)
    atendimento_id = Column (Integer, ForeignKey("atendimentos.id"), nullable=False)
    data_hora      = Column (DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    observacoes    = Column (String, nullable=True)

