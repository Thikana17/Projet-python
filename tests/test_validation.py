import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.outils.validation import code_postal, email_valide, mdp_robuste

client = TestClient(app)


# ============================================================================
# Tests unitaires : email_valide
# ============================================================================

def test_email_valide_normal():
    assert email_valide("contact@exemple.fr") is True
    assert email_valide("utilisateur.test@domaine.com") is True


def test_email_valide_limite():
    assert email_valide("nom+filtre@sous.domaine.univ-paris1.fr") is True


def test_email_valide_invalide():
    with pytest.raises(ValueError):
        email_valide("invalide")

    with pytest.raises(ValueError):
        email_valide("@domaine.com")

    with pytest.raises(ValueError):
        email_valide("utilisateur@")

    with pytest.raises(ValueError):
        email_valide("utilisateur@domaine")


# ============================================================================
# Tests unitaires : mdp_robuste
# ============================================================================

def test_mdp_robuste_normal():
    assert mdp_robuste("Secr3t!P@ss") is True


def test_mdp_robuste_limite():
    # Exactement 8 caractères avec 1 maj, 1 min, 1 chiffre, 1 spécial
    assert mdp_robuste("Aa1!bcde") is True


def test_mdp_robuste_trop_court():
    with pytest.raises(ValueError, match="au moins 8 caractères"):
        mdp_robuste("Aa1!bcd")


def test_mdp_robuste_sans_majuscule():
    with pytest.raises(ValueError, match="au moins une majuscule"):
        mdp_robuste("aa1!bcdef")


def test_mdp_robuste_sans_minuscule():
    with pytest.raises(ValueError, match="au moins une minuscule"):
        mdp_robuste("AA1!BCDEF")


def test_mdp_robuste_sans_chiffre():
    with pytest.raises(ValueError, match="au moins un chiffre"):
        mdp_robuste("Aa!bcdefg")


def test_mdp_robuste_sans_special():
    with pytest.raises(ValueError, match="au moins un caractère spécial"):
        mdp_robuste("Aa1bcdefg")


# ============================================================================
# Tests unitaires : code_postal
# ============================================================================

def test_code_postal_normal():
    assert code_postal("75001") is True
    assert code_postal("69002") is True


def test_code_postal_limite():
    assert code_postal("01000") is True
    assert code_postal("97400") is True


def test_code_postal_00000():
    with pytest.raises(ValueError, match="00000"):
        code_postal("00000")


def test_code_postal_longueur_invalide():
    with pytest.raises(ValueError):
        code_postal("7500")

    with pytest.raises(ValueError):
        code_postal("750001")


def test_code_postal_non_numerique():
    with pytest.raises(ValueError):
        code_postal("7500A")

    with pytest.raises(ValueError):
        code_postal("ABCDE")


# ============================================================================
# Tests d'intégration : routes HTTP
# ============================================================================

def test_route_email_valide():
    response = client.get("/validation/email/contact@exemple.fr")
    assert response.status_code == 200
    assert response.json() == {"email": "contact@exemple.fr", "valide": True}


def test_route_email_invalide():
    response = client.get("/validation/email/invalide")
    assert response.status_code == 400
    assert "detail" in response.json()


def test_route_mdp_valide():
    response = client.get("/validation/mdp/Secr3t!P@ss")
    assert response.status_code == 200
    assert response.json() == {"mdp": "Secr3t!P@ss", "valide": True}


def test_route_mdp_invalide():
    response = client.get("/validation/mdp/court")
    assert response.status_code == 400
    assert "detail" in response.json()


def test_route_code_postal_valide():
    response = client.get("/validation/code-postal/75001")
    assert response.status_code == 200
    assert response.json() == {"cp": "75001", "valide": True}


def test_route_code_postal_invalide():
    response = client.get("/validation/code-postal/00000")
    assert response.status_code == 400
    assert "detail" in response.json()


def test_route_code_postal_non_numerique():
    response = client.get("/validation/code-postal/7500A")
    assert response.status_code == 400
    assert "detail" in response.json()
