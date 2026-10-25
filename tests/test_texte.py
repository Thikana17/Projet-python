import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.outils.texte import est_palindrome

client = TestClient(app)

def test_est_palindrome_normal():
    assert est_palindrome("radar") == True
    assert est_palindrome("Kayak") == True 

def test_est_palindrome_limite():
    assert est_palindrome("python") == False

def test_est_palindrome_erreur():
    with pytest.raises(ValueError):
        est_palindrome("1234")

def test_route_palindrome_erreur_400():
    reponse = client.get("/palindrome/1234")
    assert reponse.status_code == 400