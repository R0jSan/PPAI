from abc import ABC, abstractmethod
from typing import List

from .IObserver import IObserver

class ISujeto(ABC):
    def __init__(self):
        self.observadores: List[IObserver] = []

    @abstractmethod
    def suscribir(self, observador):
        pass

    @abstractmethod
    def quitar(self, observador):
        pass
    
    @abstractmethod
    def notificar(self, bodega):
        pass