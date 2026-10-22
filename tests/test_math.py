import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.outils.math import pgcd

client = TestClient(app)

def test_pgcd_12_18():
    assert pgcd(12, 18) == 6

def test_pgcd_avec_zero():
    assert pgcd(0, 5) == 5

def test_pgcd_negatif():
    with pytest.raises(ValueError):
        pgcd(-4, 6)

def test_pgcd_zero_zero():
    with pytest.raises(ValueError):
        pgcd(0, 0)

def test_route_pgcd():
    r = client.get("/pgcd/12/18")
    assert r.status_code == 200
    assert r.json()["resultat"] == 6

def test_route_pgcd_negatif():
    assert client.get("/pgcd/-4/6").status_code == 400