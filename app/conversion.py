def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("La température ne peut pas être sous le zéro absolu (-273.15).")
    return (celsius * 9 / 5) + 32