from fastapi import FastAPI, HTTPException

from app.outils.math import pgcd

app = FastAPI(title="Mini API")

@app.get("/sante")
def route_sante():
    return {"statut": "API active"}

@app.get("/pgcd/{a}/{b}")
def route_pgcd(a: int, b: int):
    try:
        return {"a": a, "b": b, "resultat": pgcd(a, b)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))