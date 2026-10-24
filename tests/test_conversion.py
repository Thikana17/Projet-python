from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_celsius_fahrenheit_normal():
    reponse = client.get("/celsius_fahrenheit/0")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == 32.0

def test_celsius_fahrenheit_limite():
    reponse = client.get("/celsius_fahrenheit/-273.15")
    assert reponse.status_code == 200

def test_celsius_fahrenheit_erreur():
    reponse = client.get("/celsius_fahrenheit/-300")
    assert reponse.status_code == 400