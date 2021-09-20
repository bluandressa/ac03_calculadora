import operacao
from fabrica import *

class Calculadora:

    def calcular(self, valor1, valor2, operador):
        fabrica = OperacaoFabrica()
        return fabrica.criar(operador).executar(valor1, valor2)