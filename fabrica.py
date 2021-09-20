from operacao import *

class OperacaoFabrica():
    def criar(self, operador):
        if operador == '/':
            return Divisao
        elif operador == '+':
            return Soma
        else:
            return Subtracao
