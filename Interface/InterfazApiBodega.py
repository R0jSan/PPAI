from Entities.Vino import Vino

class InterfazApiBodega:
    def __init__(self):
        self.vinos = []
        self.fechaActualizacion = None

    """
    Recibe como parámetro el atributo nombre de un objeto bodega
    Va a recorrer un array de vinos y todos los vinos cuyo atributo bodega.nombre coincidan los va a guardar en un array y lo va a retornar
    """
    def obtenerActualizacionesVinos(self, bodegas):
        
        # Simula la obtencion de vino actualizados
        listaVinosActualizados = [
            Vino("Santa Julia", "Santa Julia Balbec", 2020, "etiqueta_anta_julia_malbec.jpg", 8500, None, None, "Frutado con notas de ciruela y moras."),
            Vino("Catena Zapata", "Catena Chardonay", 2020, "etiqueta_catena_chardonay.jpg", 6500, None, None, "Notas de frutos rojos y taninos suaves.")
        ]

        listaVinosParaActualizar = []
        for i in range(len(listaVinosActualizados)):
            for j in range(len(bodegas)):
                if listaVinosActualizados[i].bodega == bodegas[j].nombre:
                    listaVinosParaActualizar.append(listaVinosActualizados[i])
        return listaVinosParaActualizar
    

    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion
