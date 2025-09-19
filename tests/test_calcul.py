import pytest
from mon_app.calcul import addition, division


# --- tests simples ----------------------------------------------------------
def test_addition_basique():
    assert addition(2, 3) == 5


def test_division_basique():
    assert division(10, 2) == 5


# --- gestion des exceptions -------------------------------------------------
def test_division_par_zero():
    with pytest.raises(ZeroDivisionError):
        division(4, 0)


# --- paramétrage pour varier les cas ----------------------------------------
@pytest.mark.parametrize(
    "a, b, attendu",
    [
        (1, 1, 2),
        (-5, 5, 0),
        (0.1, 0.2, 0.3),
    ],
)
def test_addition_parametree(a, b, attendu):
    assert addition(a, b) == pytest.approx(attendu)
