import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$")


def email_valide(email: str) -> bool:
    """Valide le format d'un e-mail standard."""
    if not isinstance(email, str) or not EMAIL_REGEX.match(email):
        raise ValueError("Adresse e-mail invalide")
    return True


def mdp_robuste(mdp: str) -> bool:
    """Vérifie la robustesse d'un mot de passe :
    au moins 8 caractères, 1 majuscule, 1 minuscule, 1 chiffre et 1 caractère spécial.
    """
    if not isinstance(mdp, str) or len(mdp) < 8:
        raise ValueError("Le mot de passe doit contenir au moins 8 caractères")
    if not any(c.isupper() for c in mdp):
        raise ValueError("Le mot de passe doit contenir au moins une majuscule")
    if not any(c.islower() for c in mdp):
        raise ValueError("Le mot de passe doit contenir au moins une minuscule")
    if not any(c.isdigit() for c in mdp):
        raise ValueError("Le mot de passe doit contenir au moins un chiffre")
    if not any(not c.isalnum() for c in mdp):
        raise ValueError("Le mot de passe doit contenir au moins un caractère spécial")
    return True


def code_postal(cp: str) -> bool:
    """Valide un code postal français (chaîne de 5 chiffres, excluant 00000)."""
    if not isinstance(cp, str) or len(cp) != 5 or not cp.isdigit():
        raise ValueError("Le code postal doit être composé de 5 chiffres")
    if cp == "00000":
        raise ValueError("Le code postal 00000 n'est pas valide")
    return True
