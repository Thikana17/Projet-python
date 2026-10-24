from fastapi import FastAPI, HTTPException

from app.conversion import km_miles

app = FastAPI(title="Mini API")

@app.get("/sante")
def route_sante():
    return {"statut": "API active"}

@app.get("/km_miles/{km}")
def route_km_miles(km: float):
    try:
        return {"km": km, "resultat": km_miles(km)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) 


    