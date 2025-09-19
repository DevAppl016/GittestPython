def addition(a: float, b: float) -> float:
    """Additionne deux nombres."""
    return a + b


def division(a: float, b: float) -> float:
    """Division protégée contre la division par zéro."""
    if b == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro")
    return a / b


print("Module calcul chargé")
