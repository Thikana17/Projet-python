def pgcd(a: int, b: int) -> int:
    """Renvoie le plus grand commun diviseur de a et b (a, b >= 0)."""
    if a < 0 or b < 0:
        raise ValueError("a et b doivent être positifs")
    if a == 0 and b == 0:
        raise ValueError("a et b ne peuvent pas être tous les deux nuls")
    while b:
        a, b = b, a % b
    return a