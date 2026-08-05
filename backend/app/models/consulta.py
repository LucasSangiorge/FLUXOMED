from datetime     import datetime, timezone
from sqlalchemy   import Column, Integer, String, DateTime, ForeignKey
from app.database import Base


class Consulta(Base):
    __tablename__ = "consultas"

    id               = Column(Integer, primary_key=True, index=True)
    atendimento_id   = Column(Integer, ForeignKey("atendimentos.id"), nullable=False)
    descricao_medico = Column(String, nullable=False)
    data_hora        = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)