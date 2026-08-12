from fastapi                 import APIRouter, Depends, HTTPException
from sqlalchemy.orm          import Session
from app.database            import get_db
from app.models.atendimento  import Atendimento
from app.schemas.atendimento import AtendimentoCreate, AtendimentoResponse

router = APIRouter(prefix="/atendimentos", tags=["Atendimentos"])

@router.post("/", response_model=AtendimentoResponse)
def criar_atendimento(atendimento: AtendimentoCreate, db: Session = Depends(get_db)):

    novo = Atendimento(**atendimento.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[AtendimentoResponse])
def listar_atendimentos(db: Session = Depends(get_db)):
    return db.query(Atendimento).all()

@router.get("/{atendimento_id}", response_model=AtendimentoResponse)
def buscar_atendimento(atendimento_id: int, db: Session = Depends(get_db)):
    atendimento = db.query(Atendimento).filter(Atendimento.id == atendimento_id).first()
    if not atendimento:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")
    return atendimento