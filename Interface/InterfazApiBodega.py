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
            Vino("Santa Julia", "Santa Julia Malbec", 2020, "etiqueta_anta_julia_malbec.jpg", 8500, None, None,None,None, "Frutado con notas de ciruela y moras."),
            Vino("Catena Zapata", "Catena Chardonay", 2020, "etiqueta_catena_chardonay.jpg", 6500, None, None,None,None, "Notas de frutos rojos y taninos suaves."),
            Vino("Santa Julia", "Santa Julia Cabernet Sauvignon", 2017, "etiqueta_santa_julia_cabernet.jpg", 9500, None,None,None,None, "Aromas a pimiento verde y grosella negra." ),
            Vino("La Azul", "La Azul Malbec", 2016, "etiqueta_la_azul_malbec.jpg", 7500, None, None,None,None , "Sabores intensos de ciruela y especias."),
            Vino("Los Toneles", "Los Toneles Reserva", 2015, "etiqueta_los_toneles_reserva.jpg", 6500, None,None,None,None, "Cuerpo robusto con sabores de roble y frutas maduras."),
            Vino("Los Toneles", "Tonel 46", 2018, "etiqueta_los_toneles_46.jpg", 8750, None, None,None,None, "Cuerpo robusto con sabores de roble y frutas maduras."),
        ]

        listaVinosParaActualizar = []
        for i in range(len(listaVinosActualizados)):
            for j in range(len(bodegas)):
                if listaVinosActualizados[i].bodega == bodegas[j].nombre:
                    listaVinosParaActualizar.append(listaVinosActualizados[i])
        return listaVinosParaActualizar
    

    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion
