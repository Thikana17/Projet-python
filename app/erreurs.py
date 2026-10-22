class APIErreurBase(Exception):
    """Classe de base pour les erreurs de l'API."""

class NombreNegatifError(APIErreurBase):
    def __init__(self, message="Le nombre doit être positif ou nul."):
        super().__init__(message)