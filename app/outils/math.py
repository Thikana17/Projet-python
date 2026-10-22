def factorielle(n: int) -> int:
    """Renvoie n! (n doit etre >= 0)."""
    if n < 0:
        raise ValueError("n doit être positif")
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

