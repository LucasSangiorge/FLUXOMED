from fastapi              import APIRouter, Depends, HTTPException
from sqlalchemy.orm       import Session
from app.database         import get_db
from app.models.consulta  import Consulta
from app.schemas.consulta import ConsultaCreate, ConsultaResponse

router = APIRouter(prefix= "/consultas", tags=["Consultas"])

@router.post("/", response_model= ConsultaResponse)
def criar_consulta(consulta: ConsultaCreate, db: Session = Depends(get_db)):
      nova = Consulta(**consulta.model_dump())
      db.add(nova)
      db.commit()
      db.refresh(nova)
      return nova


@router.get("/", response_model=list[ConsultaResponse])
def listar_consultas(db: Session = Depends(get_db)):
      return db.query(Consulta).all()

@router.get("/{consulta_id}", response_model=ConsultaResponse)
def buscar_consulta(consulta_id: int, db: Session = Depends(get_db)):
      consulta = db.query(Consulta).filter(Consulta.id == consulta_id).first()
      if not consulta:
            raise HTTPException(status_code=404, detail="Consulta não encontrada")
      return consulta

      