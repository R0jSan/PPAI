import datetime
from Entities.Vino import Vino

class InterfazApiBodega:
    def __init__(self):
        self.vinos = []
        self.fechaActualizacion = None

    """
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
    """

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
