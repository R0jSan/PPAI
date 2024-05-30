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
        
        # Datos ficticios de vinos actualizados
        nombres_vinos = ["Santa Julia Malbec", "Santa Julia Cabernet Sauvignon", "Santa Julia Syrah"]
        anios = [2020, 2019, 2021]
        imgEtiquetas = ["etiqueta_santa_julia_malbec.jpg", "etiqueta_santa_julia_cabernet.jpg", "etiqueta_santa_julia_syrah.jpg"]
        preciosARS = [850, 950, 1050]
        maridajes = ["Carne Roja", "Quesos", "Pasta"]
        varietales = ["Malbec", "Cabernet Sauvignon", "Syrah"]
        notasCata = ["Notas de frutos rojos y taninos suaves.", "Aromas a pimiento verde y grosella negra.", "Sabores de mora y pimienta."]

        for i in range(len(nombres_vinos)):
            vino = Vino(
                bodega,
                nombres_vinos[i],
                anios[i],
                imgEtiquetas[i],
                preciosARS[i],
                maridajes[i],
                varietales[i],
                notasCata[i]
            )
            vinos_actualizados.append(vino)
        
        return vinos_actualizados
    

    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion
