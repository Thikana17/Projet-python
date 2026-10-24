from fastapi import FastAPI, HTTPException

from app.conversion import euros_devise

app = FastAPI(title="Mini API")

@app.get("/sante")
def route_sante():
    return {"statut": "API active"}

@app.get("/euros_devise/{euros}")
def route_euros_devise(euros: float):
    try:
        return {"euros": euros, "resultat": euros_devise(euros)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))