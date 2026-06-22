"""
Tests unittest pour le module calcul.
Complémentaire aux tests pytest.
"""

import unittest
from src.mon_app.calcul import addition, division


class TestAddition(unittest.TestCase):

    def test_addition_entiers(self):
        # ANCIEN : self.assertEqual(addition(2, 3), 5)
        self.assertAlmostEqual(addition(2, 3), 5, places=9,
                               msg="2 + 3 doit valoir 5")

    def test_addition_flottants(self):
        self.assertAlmostEqual(addition(0.1, 0.2), 0.3, places=9,
                               msg="0.1 + 0.2 doit approcher 0.3")

    def test_addition_negatifs(self):
        self.assertAlmostEqual(addition(-5, 5), 0, places=9)


class TestDivision(unittest.TestCase):

    def test_division_basique(self):
        # ANCIEN : self.assertEqual(division(10, 2), 5)
        self.assertAlmostEqual(division(10, 2), 5.0, places=9)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(4, 0)

    def test_division_type_invalide(self):
        # NOUVEAU
        with self.assertRaises(TypeError):
            division("texte", 2)

    def test_division_negatif(self):
        self.assertAlmostEqual(division(-10, 2), -5.0, places=9)


if __name__ == "__main__":
    unittest.main(verbosity=2)
