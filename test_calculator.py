import unittest
from calculadora import Calculadora

class TestCalculator(unittest.TestCase):
    def testDivisao(self):
        self.assertEqual(calculadora.calcular(150,3, '/'),50)

    def testSoma(self):
        self.assertEqual(calculadora.calcular(250,3, '+'),253)

    def testSubtracao(self):
        self.assertEqual(calculadora.calcular(40,5, '-'),35)


if __name__ == '__main__':
    calculadora = Calculadora()
    unittest.main()



