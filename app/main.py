from fastapi import FastAPI, HTTPException

from app.outils.texte import est_palindrome

app = FastAPI(title="Mini API")

@app.get("/sante")
def route_sante():
    return {"statut": "API active"}

@app.get("/palindrome/{mot}")
def route_palindrome(mot: str):
    try:
        return {"mot": mot, "resultat": est_palindrome(mot)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))