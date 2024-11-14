from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def actualizar(self, usuarios, bodega):
        pass