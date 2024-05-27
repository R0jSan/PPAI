from Entities.Vino import Vino
from Interface.InterfazApiBodega import InterfazApiBodega


class GestorImportacionNovedades:
    def __init__(self, pantallaImportacionNovedades):
        self.bodegas = []
        self.bodegasActualizables = []
        self.nombreBodegasActualizables = []
        self.pantallaImportacionNovedades = pantallaImportacionNovedades
        self.maridajes = []
        self.vinosActualizables = []

    def opcionImportarActualizacionVinos(self):
        self.buscarBodegasActualizables()
        self.pantallaImportacionNovedades.mostrarBodegasActualizables(self.bodegasActualizables)
        self.pantallaImportacionNovedades.seleccionar_bodega_button.clicked.connect(self.procesarBodegaSeleccionada)

    def procesarBodegaSeleccionada(self):
        bodegaSeleccionada = self.pantallaImportacionNovedades.tomarBodegasSeleccionada()
        if bodegaSeleccionada is not None:
            actualizacionesVinos = self.obtenerActVinosBodegaSeleccionada(bodegaSeleccionada)
            self.obtenerVinosActualizables(bodegaSeleccionada, actualizacionesVinos)
            self.actualizarOCrearVinos(bodegaSeleccionada, self.vinosActualizables)
            self.pantallaImportacionNovedades.mostrarVinosActualizados(bodegaSeleccionada, self.vinosActualizables)
            self.pantallaImportacionNovedades.stacked_widget.setCurrentIndex(2)  # Cambiar a la vista de vinos actualizados

    def buscarBodegasActualizables(self):
        self.bodegasActualizables.clear()
        for bodega in self.bodegas:
            if bodega.sePuedeActualizarNovedades():
                self.bodegasActualizables.append(bodega)

    def obtenerActVinosBodegaSeleccionada(self, bodegaSeleccionada):
        return InterfazApiBodega().obtenerActualizacionesVinos(bodegaSeleccionada)
    
    def obtenerVinosActualizables(self, bodegaSeleccionada, actualizacionesVinos):
        vinosActualizables = []
        for vino in actualizacionesVinos:
            if bodegaSeleccionada.tenesEsteVino(vino):
                vinosActualizables.append(vino)
        self.vinosActualizables = vinosActualizables

    def actualizarOCrearVinos(self, bodegaSeleccionada, vinosActualizables):
        for vino in vinosActualizables:
            if bodegaSeleccionada.tenesEsteVino(vino):
                self.actualizarCaracteristicasVinoExistente(vino)
            else:
                self.crearVino(vino)
    
    def actualizarCaracteristicasVinoExistente(self, vino):
        InterfazApiBodega().actualizarDatosVino(vino)

    def determinarVinosActualizar(self):
        pass

    def crearVino(self, vino):
        # Crear un nuevo vino en la bodega seleccionada
        self.buscarMaridaje(vino.maridaje)
        vinoNuevo = Vino(vino.bodega, vino.nombre, vino.anio, vino.imgEtiqueta, vino.precioARS, vino.maridaje, vino.varietal, vino.notaCata)
        vino.bodega.addVino(vinoNuevo)

    def buscarMaridaje(self, maridaje):
        for maridaje in self.maridajes:
            maridaje.sosMaridaje() 

    def buscarSeguidoresBodega(self):
        pass
