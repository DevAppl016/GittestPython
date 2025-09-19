import unittest
from mon_app.calcul import addition, division


class TestCalcul(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(4, 0)


if __name__ == "__main__":
    unittest.main()
