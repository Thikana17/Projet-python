from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_euros_devise_normal():
    reponse = client.get("/euros_devise/10")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == 10.5

def test_euros_devise_limite():
    reponse = client.get("/euros_devise/0")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == 0.0

def test_euros_devise_erreur():
    reponse = client.get("/euros_devise/-5")
    assert reponse.status_code == 400