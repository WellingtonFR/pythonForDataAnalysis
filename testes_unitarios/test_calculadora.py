import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        calculadora = Calculadora()
        resultado = calculadora.somar(5, 3)
        self.assertEqual(resultado, 9, "A soma de 5 e 3 deve ser 8")


if __name__ == "__main__":
    unittest.main()
