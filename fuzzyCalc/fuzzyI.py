from abc import ABC, abstractmethod

class FuzzyNumber(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def suma(self):
        pass

    @abstractmethod
    def resta(self):
        pass

    @abstractmethod
    def multiplicacion(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def trapezoidal(self):
        pass