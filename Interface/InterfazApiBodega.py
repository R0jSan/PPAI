import datetime
from Entities.Vino import Vino

class InterfazApiBodega:
    def __init__(self):
        self.vinos = []
        self.fechaActualizacion = None

    """
    Recibe como parámetro el atributo nombre de un objeto bodega
    Va a recorrer un array de vinos y todos los vinos cuyo atributo bodega.nombre coincidan los va a guardar en un array y lo va a retornar
    """
    def obtenerActualizacionesVinos(self, bodegaNombre=str()):
        
        # Simula la obtencion de vino actualizados
        listaVinosActualizados = [
            Vino("Santa Julia", "Santa Julia Balbec", 2020, "etiqueta_anta_julia_malbec.jpg", 8500, None, None, "Frutado con notas de ciruela y moras."),
    
        ]

        listaVinosParaActualizar = []
        for i in range(len(listaVinosActualizados)):
            if listaVinosActualizados[i].bodega == bodegaNombre:
                listaVinosParaActualizar.append(listaVinosActualizados[i])
        return listaVinosParaActualizar
    

    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion
