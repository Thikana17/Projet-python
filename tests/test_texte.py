from fastapi.testclient import TestClient

from app.main import app
from app.outils.texte import compter_voyelles, inverser

client = TestClient(app)

def test_compter_voyelles_logique():
    assert compter_voyelles("bonjour") == 3
    assert compter_voyelles("HETIC") == 2
    assert compter_voyelles("brrr") == 0

def test_route_voyelles():
    reponse = client.get("/voyelles?texte=python")
    assert reponse.status_code == 200
    assert reponse.json() == {"texte": "python", "nombre_voyelles": 2}

def test_inverser_logique():
    assert inverser("HETIC") == "CITEH"
    assert inverser("bonjour") == "ruojnob"

def test_route_inverser():
    reponse = client.get("/inverser?texte=python")
    assert reponse.status_code == 200
    assert reponse.json() == {"texte_original": "python", "texte_inverse": "nohtyp"}