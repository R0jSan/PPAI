from Entities.Vino import Vino
from Entities.Varietal import Varietal
from Entities.TipoUva import TipoUva

class InterfazApiBodega:
    def __init__(self):
        self.vinos = []
        self.fechaActualizacion = None

    """
    Recibe como parámetro el atributo nombre de un objeto bodega.
    Va a recorrer un array de vinos y todos los vinos cuyo atributo bodega.nombre coincidan los va a guardar en un array y lo va a retornar.
    """
    def obtenerActualizacionesVinos(self, bodegas):
        
        
        tipo_uva_malbec = TipoUva("Malbec", "Variedad de uva tinta argentina")
        tipo_uva_chardonnay = TipoUva("Chardonnay", "Variedad de uva blanca")
        tipo_uva_cabernet = TipoUva("Cabernet Sauvignon", "Variedad clásica de uva tinta")

        varietal_malbec = Varietal("Varietal Malbec", 100, tipo_uva_malbec)
        varietal_chardonnay = Varietal("Varietal Chardonnay", 100, tipo_uva_chardonnay)
        varietal_cabernet = Varietal("Varietal Cabernet", 100, tipo_uva_cabernet)
        varietal_blend = Varietal("Blend Malbec y Cabernet", 60, tipo_uva_malbec)
        varietal_blend.setPorcentajeUva(60)
        varietal_blend.setTipoUva(tipo_uva_cabernet)  

        # Simula la obtención de vinos actualizados con múltiples varietales
        lista_vinos_actualizados = [
            Vino("Santa Julia", "Santa Julia Malbec", 2020, "etiqueta_santa_julia_malbec.jpg", 8500, None, "Frutado con notas de ciruela y moras."),
            Vino("Catena Zapata", "Catena Chardonnay", 2020, "etiqueta_catena_chardonnay.jpg", 6500, None, "Notas de frutos rojos y taninos suaves."),
            Vino("Santa Julia", "Santa Julia Cabernet Sauvignon", 2017, "etiqueta_santa_julia_cabernet.jpg", 9500, None, "Aromas a pimiento verde y grosella negra."),
            Vino("La Azul", "La Azul Malbec", 2016, "etiqueta_la_azul_malbec.jpg", 7500, None, "Sabores intensos de ciruela y especias."),
            Vino("Los Toneles", "Los Toneles Reserva", 2015, "etiqueta_los_toneles_reserva.jpg", 6500, None, "Cuerpo robusto con sabores de roble y frutas maduras."),
            Vino("Los Toneles", "Tonel 46", 2018, "etiqueta_los_toneles_46.jpg", 8750, None, "Cuerpo robusto con sabores de roble y frutas maduras."),
        ]

        lista_vinos_actualizados[0].agregarVarietal("Varietal Malbec", 100, tipo_uva_malbec)  # Santa Julia Malbec
        lista_vinos_actualizados[1].agregarVarietal("Varietal Chardonnay", 100, tipo_uva_chardonnay)  # Catena Chardonnay
        lista_vinos_actualizados[2].agregarVarietal("Varietal Cabernet", 100, tipo_uva_cabernet)  # Santa Julia Cabernet Sauvignon
        lista_vinos_actualizados[3].agregarVarietal("Blend Malbec y Cabernet", 60, tipo_uva_malbec)
        lista_vinos_actualizados[3].agregarVarietal("Blend Malbec y Cabernet", 40, tipo_uva_cabernet)  # La Azul Malbec con blend de Malbec y Cabernet
        lista_vinos_actualizados[4].agregarVarietal("Varietal Malbec", 60, tipo_uva_malbec)
        lista_vinos_actualizados[4].agregarVarietal("Varietal Cabernet", 40, tipo_uva_cabernet)  # Los Toneles Reserva
        lista_vinos_actualizados[5].agregarVarietal("Varietal Chardonnay", 50, tipo_uva_chardonnay)
        lista_vinos_actualizados[5].agregarVarietal("Varietal Cabernet", 50, tipo_uva_cabernet)  # Tonel 46

        lista_vinos_para_actualizar = []
        for vino in lista_vinos_actualizados:
            for bodega in bodegas:
                if vino.bodega == bodega.nombre:
                    lista_vinos_para_actualizar.append(vino)

        return lista_vinos_para_actualizar
    
    def setFechaActualizacion(self, fecha_actualizacion):
        self.fechaActualizacion = fecha_actualizacion
