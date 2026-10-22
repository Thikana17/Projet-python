from app.erreurs import APIErreurBase, NombreNegatifError


def test_instanciation_erreurs():
    erreur = NombreNegatifError()
    assert isinstance(erreur, APIErreurBase)
    assert str(erreur) == "Le nombre doit être positif ou nul."