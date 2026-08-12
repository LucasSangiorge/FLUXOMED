from fastapi             import APIRouter, Depends, HTTPException
from sqlalchemy.orm      import Session
from app.database        import get_db
from app.models.triagem  import Triagem
from app.schemas.triagem import TriagemCreate, TriagemResponse

router = APIRouter(prefix="/triagens", tags=["Triagens"])

@router.post("/", response_model=TriagemResponse)
def   criar_triagens(triagem: TriagemCreate, db: Session = Depends(get_db)):
      nova = Triagem(**triagem.model_dump())
      db.add(nova)
      db.commit()
      db.refresh(nova)
      return nova

@router.get("/", response_model= list[TriagemResponse])
def   listar_triagens(db: Session = Depends(get_db)):
      return db.query(Triagem).all()

@router.get("/{triagem_id}", response_model=TriagemResponse)
def   buscar_triagem(triagem_id:int, db:Session = Depends(get_db)):
      triagem = db.query(Triagem).filter(Triagem.id == triagem_id).first()
      if not triagem:
            raise HTTPException(status_code=404, detail="Triagem não encontrada")
      return triagem

