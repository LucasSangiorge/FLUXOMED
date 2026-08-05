import enum
from   datetime     import datetime, timezone
from   sqlalchemy   import Column, Integer, String, DateTime, Enum, ForeignKey
from   app.database import Base


class CorClassificacaoEnum(str, enum.Enum):
    VERMELHO  = "Vermelho"
    LARANJA   = "Laranja"
    AMARELO   = "Amarelo"
   
class Triagem(Base):
    __tablename__ = "triagens"

    id                = Column (Integer, primary_key=True, index=True)
    atendimento_id    = Column (Integer, ForeignKey("atendimentos.id"), nullable=False)
    sintomas          = Column (String, nullable=False)
    pressao_arterial  = Column (String, nullable=False)
    cor_classificacao = Column (Enum(CorClassificacaoEnum), nullable=False)
    data_hora         = Column (DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    