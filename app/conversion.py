def km_miles(km: float) -> float:
    if km < 0:
        raise ValueError("La distance en kilomètres ne peut pas être négative.")
    return km * 0.621371