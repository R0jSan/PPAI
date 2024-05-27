from Interface.InterfazApiBodega import InterfazApiBodega
from Interface.PantallaImportacionNovedades import PantallaImportacionNovedades

class GestorImportacionNovedades:

    def __init__(self,pantallaImportacionNovedades):
        self.bodegas = []
        self.bodegasActualizables = []
        self.nombreBodegasActualizables = []
        self.pantallaImportacionNovedades = pantallaImportacionNovedades

    def opcionImportarActualizacionVinos(self):
        self.buscarBodegasActualizables()
        self.pantallaImportacionNovedades.mostrarBodegasActualizables(self.nombreBodegasActualizables)
        bodegaSeleccionada = self.pantallaImportacionNovedades.tomarBodegasSeleccionada()
        actualizacionesVinos = self.obtenerActVinosBodegaSeleccionada(bodegaSeleccionada)
        self.obtenerVinosActualizables(bodegaSeleccionada)


    def buscarBodegasActualizables(self):

        #Busca desde las bodegas que estan en periodo de actualizacion, las guarda en la lista bodegasActualizables junto a su nombre
        # en la lista NombreBodegasActualizables (los cuales deberian tener el mismo indice)

        for bodega in self.bodegas:

            if bodega.sePuedeActualizarNovedades():
                self.bodegasActualizables.append(bodega)
                self.nombreBodegasActualizables.append(bodega.getNombre())

    def obtenerActVinosBodegaSeleccionada(self, bodegaSeleccionada):
        return InterfazApiBodega().obtenerActualizacionesVinos(bodegaSeleccionada)
    
    def obtenerVinosActualizables(self, bodegaSeleccionada):
        pass

    def determinarVinosActualizar():
        pass

    def actualizarOCrearVinos():
        pass

    def actualizarVinoExistente():
        pass

    def crearVino():
        #vino = Vino(bodega, nombre, random.randint(2000, 2024), None, random.randint(2000,5000))
        pass

    def buscarSeguidoresBodega():
        pass