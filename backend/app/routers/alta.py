from fastapi          import APIRouter, Depends, HTTPException
from sqlalchemy.orm   import Session
from app.database     import get_db
from app.models.alta  import Alta
from app.schemas.alta import AltaCreate, AltaResponse

router = APIRouter(prefix="/altas", tags=["Altas"])

@router.post("/", response_model=AltaResponse)
def criar_alta(alta: AltaCreate, db:Session = Depends(get_db)):
      novo = Alta(**alta.model_dump())
      db.add(novo)
      db.commit()
      db.refresh(novo)
      return novo

@router.get("/",response_model=list[AltaResponse])
def listar_alta(db:Session = Depends(get_db)):
      return db.query(Alta).all()



@router.get("/{alta_id}", response_model=AltaResponse)
def buscar_alta(alta_id:int , db:Session = Depends(get_db)):
      alta = db.query(Alta).filter(Alta.id == alta_id).first()
      if not alta:
            raise HTTPException(status_code=404, detail="Alta não existe")
      return alta

