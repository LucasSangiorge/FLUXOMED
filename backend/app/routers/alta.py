from fastapi                    import APIRouter, Depends, HTTPException
from sqlalchemy.orm             import Session
from app.database                import get_db
from app.models.alta            import Alta
from app.models.atendimento     import StatusAtendimentoEnum
from app.schemas.alta           import AltaCreate, AltaResponse
from app.services.regras_negocio import validar_alta

router = APIRouter(prefix="/altas", tags=["Altas"])

@router.post("/", response_model=AltaResponse)
def criar_alta(alta: AltaCreate, db:Session = Depends(get_db)):
      atendimento = validar_alta(alta.atendimento_id, db)

      novo = Alta(**alta.model_dump())
      db.add(novo)

      atendimento.status = StatusAtendimentoEnum.CONCLUIDO

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

