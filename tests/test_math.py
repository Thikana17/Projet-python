import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.outils.math import factorielle

client = TestClient(app)

# --- factorielle ---
def test_factorielle_de_5():
    assert factorielle(5) == 120

def test_factorielle_de_0():
    assert factorielle(0) == 1

def test_factorielle_negative():
    with pytest.raises(ValueError):
        factorielle(-1)

def test_route_factorielle():
    r = client.get("/factorielle/5")
    assert r.status_code == 200
    assert r.json()["resultat"] == 120

def test_route_factorielle_negative():
    assert client.get("/factorielle/-1").status_code == 400