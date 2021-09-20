from abc import ABC, abstractclassmethod

class Ioperacao(ABC):

    @abstractclassmethod
    def executar(self, valor1, valor2):
        pass