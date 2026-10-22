import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.outils.math import est_premier

client = TestClient(app)

def test_est_premier_17():
    assert est_premier(17) is True

def test_est_premier_limites():
    assert est_premier(0) is False
    assert est_premier(1) is False
    assert est_premier(2) is True

def test_est_premier_negatif():
    with pytest.raises(ValueError):
        est_premier(-3)

def test_route_est_premier():
    r = client.get("/est_premier/17")
    assert r.status_code == 200
    assert r.json()["resultat"] is True

def test_route_est_premier_negatif():
    assert client.get("/est_premier/-3").status_code == 400