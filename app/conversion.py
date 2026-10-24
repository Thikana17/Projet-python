def euros_devise(euros: float) -> float:
    if euros < 0:
        raise ValueError("Le montant en euros ne peut pas être négatif.")
    return euros * 1.05