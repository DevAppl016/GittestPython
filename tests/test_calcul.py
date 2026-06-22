"""
Tests pytest pour le module calcul.
Couvre : cas normaux, limites, exceptions, types invalides.
"""

import pytest
from src.mon_app.calcul import addition, division


# ── Fixtures ────────────────────────────────────────────────

@pytest.fixture
def valeurs_positives():
    """Paire de valeurs positives standard."""
    return 10.0, 2.0


# ── Addition ────────────────────────────────────────────────

class TestAddition:

    def test_entiers_positifs(self):
        # ANCIEN : assert addition(2, 3) == 5
        assert addition(2, 3) == pytest.approx(5)

    def test_entiers_negatifs(self):
        assert addition(-5, -3) == pytest.approx(-8)

    def test_zero(self):
        assert addition(0, 0) == pytest.approx(0)

    def test_flottants(self):
        # ANCIEN : cas fragile sans approx correcte
        assert addition(0.1, 0.2) == pytest.approx(0.3, rel=1e-9)

    @pytest.mark.parametrize("a, b, attendu", [
        (1,    1,   2),
        (-5,   5,   0),
        (0.1,  0.2, 0.3),
        (1e10, 1,   1e10 + 1),   # NOUVEAU : grands nombres
        (-1e10, 1e10, 0),        # NOUVEAU : annulation
    ])
    def test_parametree(self, a, b, attendu):
        assert addition(a, b) == pytest.approx(attendu, rel=1e-9)


# ── Division ────────────────────────────────────────────────

class TestDivision:

    def test_basique(self, valeurs_positives):
        a, b = valeurs_positives
        assert division(a, b) == pytest.approx(5.0)

    def test_division_par_zero(self):
        with pytest.raises(ZeroDivisionError, match="zéro"):
            division(4, 0)

    def test_type_invalide(self):
        # NOUVEAU : cas que le recruteur veut voir
        with pytest.raises(TypeError):
            division("dix", 2)

    def test_negatifs(self):
        assert division(-10, 2) == pytest.approx(-5.0)

    def test_flottant(self):
        assert division(1, 3) == pytest.approx(0.3333, rel=1e-4)

    @pytest.mark.parametrize("a, b, attendu", [
        (10,  2,  5.0),
        (-10, 2, -5.0),
        (7,   2,  3.5),
        (0,   5,  0.0),   # NOUVEAU : zéro au numérateur
    ])
    def test_parametree(self, a, b, attendu):
        assert division(a, b) == pytest.approx(attendu)
