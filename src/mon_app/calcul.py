"""
Module de calculs mathématiques de base.
Toutes les fonctions sont typées et documentées.
"""

import logging

logger = logging.getLogger(__name__)


def addition(a: float, b: float) -> float:
    """
    Additionne deux nombres réels.

    Args:
        a: Premier opérande.
        b: Deuxième opérande.

    Returns:
        La somme de a et b.

    Examples:
        >>> addition(2, 3)
        5
        >>> addition(-1, 1)
        0
    """
    result = a + b
    logger.debug("addition(%s, %s) = %s", a, b, result)
    return result


def division(a: float, b: float) -> float:
    """
    Divise a par b avec protection contre la division par zéro.

    Args:
        a: Numérateur.
        b: Dénominateur (ne doit pas être zéro).

    Returns:
        Le quotient a / b.

    Raises:
        ZeroDivisionError: Si b vaut 0.
        TypeError: Si a ou b ne sont pas des nombres.

    Examples:
        >>> division(10, 2)
        5.0
    """
    # ANCIEN : pas de vérification de type
    # NOUVEAU : vérification complète
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
 raise TypeError(
    f"Les opérandes doivent être des nombres, reçu : {type(a)}, {type(b)}"
 )

    if b == 0:
        raise ZeroDivisionError(f"Impossible de diviser {a} par zéro")

    result = a / b
    logger.debug("division(%s, %s) = %s", a, b, result)
    return result
