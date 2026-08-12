from fastapi           import APIRouter, Depends, HTTPException
from sqlalchemy.orm    import Session
from app.database      import get_db
from app.models.exame  import Exame
from app.schemas.exame import ExameCreate, ExameResponse

router = APIRouter(prefix="/exame", tags=["Exame"])

@router.post("/", response_model= ExameResponse)
def criar_exame(exame: ExameCreate, db:Session = Depends(get_db)):
      novo = Exame(**exame.model_dump())
      db.add(novo)
      db.commit()
      db.refresh(novo)
      return novo


@router.get("/", response_model=list[ExameResponse])
def listar_exame(db:Session = Depends(get_db)):
      return db.query(Exame).all()


@router.get("/{exame_id}", response_model=ExameResponse)
def buscar_exame(exame_id: int, db:Session = Depends(get_db)):
      exame = db.query(Exame).filter(Exame.id == exame_id).first()
      if not exame:
            raise HTTPException(status_code=404, detail="Exame não encontrado")
      return exame