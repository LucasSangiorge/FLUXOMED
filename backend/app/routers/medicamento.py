from fastapi                 import APIRouter, Depends, HTTPException
from sqlalchemy.orm          import Session
from app.database            import get_db
from app.models.medicacao    import Medicamento
from app.schemas.medicamento import MedicamentoCreate, MedicamentoResponse

router = APIRouter(prefix=("/medicamentos"), tags=["Medicamentos"])

@router.post("/", response_model=MedicamentoResponse)
def criar_medicamento(medicamento: MedicamentoCreate, db:Session = Depends(get_db)):
      novo = Medicamento(**medicamento.model_dump())
      db.add(novo)
      db.commit()
      db.refresh(novo)
      return novo

@router.get("/", response_model=list[MedicamentoResponse])
def listar_medicamento(db:Session = Depends(get_db)):
      return db.query(Medicamento).all()


@router.get("/{medicamento_id}", response_model=MedicamentoResponse)
def buscar_medicamento(medicamento_id:int, db:Session = Depends(get_db)):
      medicamento = db.query(Medicamento).filter(Medicamento.id == medicamento_id).first()
      if not medicamento:
            raise HTTPException(status_code=404, detail="Medicamento não existe")
      return medicamento