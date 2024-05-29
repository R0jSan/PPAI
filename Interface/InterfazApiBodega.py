import datetime
import random
from Entities.Vino import Vino

class InterfazApiBodega:
    def __init__(self):
        self.vinos = []
        self.fechaActualizacion = None

    def obtenerActualizacionesVinos(self, bodega):
        # Simula la obtención de actualizaciones de vinos con datos completos
        vinos_actualizados = []
        
        nombre = "Santa Julia Malbec"
        anio = 2020
        imgEtiqueta = "etiqueta_santa_julia_malbec.jpg"
        precioARS = random.randint(800, 2000)
        maridaje = f"Maridaje 1"
        varietal = f"Varietal 1"
        notaCata = "Notas de frutos rojos y taninos suaves."
            
        vino = Vino(bodega, nombre, anio, imgEtiqueta, precioARS, maridaje, varietal, notaCata)
        vinos_actualizados.append(vino)
        
        return vinos_actualizados
    

    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion
