def est_premier(n: int) -> bool:
    """Renvoie True si n est un nombre premier (n doit etre >= 0)."""
    if n < 0:
        raise ValueError("n doit être positif")
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

