from fastapi import FastAPI, HTTPException

from app.outils.math import est_premier

app = FastAPI(title="Mini API")

@app.get("/sante")
def route_sante():
    return {"statut": "API active"}

@app.get("/est_premier/{n}")
def route_est_premier(n: int):
    try:
        return {"n": n, "resultat": est_premier(n)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))