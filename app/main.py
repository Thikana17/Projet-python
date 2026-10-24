from fastapi import FastAPI, HTTPException

from app.conversion import celsius_fahrenheit

app = FastAPI(title="Mini API")

@app.get("/sante")
def route_sante():
    return {"statut": "API active"}

@app.get("/celsius_fahrenheit/{celsius}")
def route_celsius_fahrenheit(celsius: float):
    try:
        return {"celsius": celsius, "resultat": celsius_fahrenheit(celsius)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))