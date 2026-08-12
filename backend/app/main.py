from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import atendimento, paciente, triagem, consulta, exame, alta, medicamento, fila_espera


app = FastAPI(
    title="FluxoMed",
    description="API de fluxo de Pronto Socorro — do cadastro do paciente até a alta hospitalar.",
    version="0.4.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(atendimento.router)
app.include_router(paciente.router)
app.include_router(triagem.router)
app.include_router(consulta.router)
app.include_router(exame.router)
app.include_router(alta.router)
app.include_router(medicamento.router)
app.include_router(fila_espera.router)



@app.get("/")
def read_root():
    return {"Status": "FluxoMed API no ar"}

