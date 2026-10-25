from fastapi import FastAPI

from app.outils.texte import compter_voyelles, inverser

app = FastAPI(title="Mini API")

@app.get("/sante")
def route_sante():
    return {"statut": "API active"}
@app.get("/voyelles")
def route_compter_voyelles(texte: str):
    compte = compter_voyelles(texte)
    return {"texte": texte, "nombre_voyelles": compte}
@app.get("/inverser")
def route_inverser(texte: str):
    resultat = inverser(texte)
    return {"texte_original": texte, "texte_inverse": resultat}