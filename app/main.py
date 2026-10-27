from fastapi import FastAPI, HTTPException

from app.conversion import celsius_fahrenheit
from app.outils.math import factorielle
from app.outils.validation import code_postal, email_valide, mdp_robuste

app = FastAPI(title="Mini API")


@app.get("/sante")
def route_sante():
    return {"statut": "API active"}

@app.get("/celsius_fahrenheit/{celsius}")
def route_celsius_fahrenheit(celsius: float):
    try:
        return {"celsius": celsius, "resultat": celsius_fahrenheit(celsius)}

@app.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/validation/email/{email}")
def route_validation_email(email: str):
    try:
        return {"email": email, "valide": email_valide(email)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/validation/mdp/{mdp}")
def route_validation_mdp(mdp: str):
    try:
        return {"mdp": mdp, "valide": mdp_robuste(mdp)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/validation/code-postal/{cp}")
def route_validation_code_postal(cp: str):
    try:
        return {"cp": cp, "valide": code_postal(cp)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))