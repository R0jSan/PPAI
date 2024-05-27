import random
import requests

class InterfazApiBodega:
    def obtenerActualizacionesVinos(self, bodega):
        return [f"Vino {i} - {bodega}" for i in range(1, random.randint(2, 10))]