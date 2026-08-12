from fastapi              import APIRouter, Depends, HTTPException
from sqlalchemy.orm       import Session
from app.database         import get_db
from app.models.paciente           import Paciente
from app.schemas.paciente import PacienteCreate, PacienteResponse

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

@router.post("/", response_model= PacienteResponse)
def criar_paciente(paciente: PacienteCreate, db:Session = Depends(get_db)):
      novo = Paciente(**paciente.model_dump())
      db.add(novo)
      db.commit()
      db.refresh(novo)
      return novo

@router.get("/", response_model=list[PacienteResponse])
def listar_pacientes(db:Session = Depends(get_db)):
      return db.query(Paciente).all()

@router.get("/{paciente_id}", response_model= PacienteResponse)
def buscar_paciente(paciente_id: int, db:Session = Depends(get_db)):
      paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
      if not paciente:
            raise HTTPException(status_code=404, detail="Paciente não encontrado")
      return paciente