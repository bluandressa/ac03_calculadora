from interface import Ioperacao

class Divisao(Ioperacao):
    def executar(valor1, valor2):
        return valor1/valor2

class Soma(Ioperacao):
    def executar(valor1, valor2):
        return valor1 + valor2

class Subtracao(Ioperacao):
    def executar(valor1, valor2):
        return valor1-valor2