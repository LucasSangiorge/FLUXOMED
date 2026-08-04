from fastapi import FastAPI

app = FastAPI(title="FluxoMed")

@app.get("/")
def read_root():
    return {"Status": "FluxoMed API no ar"}