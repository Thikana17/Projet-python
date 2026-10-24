from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_km_miles_normal():
    reponse = client.get("/km_miles/10")
    assert reponse.status_code == 200
    assert round(reponse.json()["resultat"], 4) == 6.2137

def test_km_miles_limite():
    reponse = client.get("/km_miles/0")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == 0.0

def test_km_miles_erreur():
    reponse = client.get("/km_miles/-5")
    assert reponse.status_code == 400