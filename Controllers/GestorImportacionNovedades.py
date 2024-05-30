from Entities.Vino import Vino
from Interface.InterfazApiBodega import InterfazApiBodega
from datetime import datetime

class GestorImportacionNovedades:
    apiBodega = InterfazApiBodega() # no se donde iria esto
    def __init__(self, pantallaImportacionNovedades):
        self.bodegas = [] # Son todas la bodegas
        self.bodegasActualizables = [] # Son las bodegas que se pueden actualizar
        self.nombreBodegasActualizables = [] # Son el nombre de las bodegas que se pueden actualizar
        self.pantallaImportacionNovedades = pantallaImportacionNovedades # Es la pantalla
        self.maridajes = []
        self.tiposUvas = []
        self.vinosActualizables = [] # Los vinos que se van a actualizar
        self.fechaActual = None # Es la fecha actual calculada por el gestor
        self.bodegaSeleccionPantalla = []
        self.enofilos = []

    """
    funcion opcionImportarActualizacionVinos()
    Se ejecuta primero esta funcion, llama a la funcion del gestor calcularFechaActual(),
    despues llama a la funcion del gestor buscarBodegasActualizables()
    mostrarBodegasActualizables() muestra en la pantalla cada bodega habilitada a actualizar
    en seleccionar_bodega_button.clicked.connect() recib
    """
    def opcionImportarActualizacionVinos(self):
        self.calcularFechaActual()
        self.buscarBodegasActualizables()
        self.pantallaImportacionNovedades.mostrarBodegasActualizables(self.nombreBodegasActualizables)
        self.pantallaImportacionNovedades.seleccionar_bodega_button.clicked.connect(self.tomarBodegasSeleccionada)

    """
    Calcula la fecha actual y la guarda en una variable
    """
    def calcularFechaActual(self):
        self.fechaActual = datetime.now()

    """
    Funcion buscarBodegasActualizables()
    Busca la bodegas que necesiten actualizarse segun el periodo de actualizacion
    Guarda cada bodega habilitada en la variable del gestor bodegasActualizables en un array
    Tambien guarda el nombre de cada bodega habilitada en la variable nombreBodegasActualizables en un array
    """
    def buscarBodegasActualizables(self):
        self.bodegasActualizables.clear()
        for bodega in self.bodegas:
            if bodega.sePuedeActualizarNovedades(self.fechaActual):
                self.bodegasActualizables.append(bodega)
                self.nombreBodegasActualizables.append(bodega.getNombre()) # modificado

    """
    funcion procesarBodegaSeleccionada()
    el atributo del gestor "bodegaSeleccionPantalla" guarda un array con las bodegas seleccionadas
    luego recorre cada bodega para obtener los vinos actualizados con la funcion del gestor obtenerVinosActualizables()
    y con la funcion actualizarOCrearVinos() modifica los ya existentes o crea los que no existan
    """
    def tomarBodegasSeleccionada(self):
        # self.bodegaSeleccionPantalla es un array de objetos QListWidgetItem, tengo que aplicarle .text() para filtrar
        
        self.bodegaSeleccionPantalla = self.pantallaImportacionNovedades.tomarBodegasSeleccionada()
        if self.bodegaSeleccionPantalla:
            for i in range(len(self.bodegaSeleccionPantalla)):
                for bodega in self.bodegasActualizables:
                    if bodega.nombre == self.bodegaSeleccionPantalla[i].text():
                        actualizacionesVinos = self.obtenerActVinosBodegaSeleccionada(bodega.nombre)
                        self.obtenerVinosActualizables(actualizacionesVinos, bodega)
                        self.actualizarOCrearVinos(bodega, self.vinosActualizables)
                        self.apiBodega.setFechaActualizacion(self.fechaActual)
                        self.pantallaImportacionNovedades.mostrarVinosActualizados(bodega, self.vinosActualizables)
                        self.pantallaImportacionNovedades.stacked_widget.setCurrentIndex(2)  # Cambiar a la vista de vinos actualizados

                        # -----------Es para testear
                        # print(f"Bodega: {bodega.nombre} == {self.bodegaSeleccionPantalla[i].text()}")

    """
    Funcion obtenerActVinosBodegaSeleccionada()
    devuelve un array con lo vinos actualizados que tiene la API
    """
    def obtenerActVinosBodegaSeleccionada(self, bodegaSeleccionada):
        return self.apiBodega.obtenerActualizacionesVinos(bodegaSeleccionada)

    """
    funcion obtenerVinosActualizables()
    El parametro "actualizacionesVinos" contiene un array con los vinos a modificar
    """
    def obtenerVinosActualizables(self, actualizacionesVinos, bodega):
        vinosActualizables = []
        for vino in actualizacionesVinos:
            if bodega.tenesEsteVino(vino): # Modificado
                vinosActualizables.append(vino)
        self.vinosActualizables = vinosActualizables


    def actualizarOCrearVinos(self, bodegaSeleccionada, vinosActualizables):
        for vino in vinosActualizables:
            if bodegaSeleccionada.tenesEsteVino(vino):
                self.actualizarCaracteristicasVinoExistente(vino,bodegaSeleccionada)
            else:
                self.crearVino(vino)
    
    def actualizarCaracteristicasVinoExistente(self, vino,bodega):
        bodega.actualizarDatosVino(vino)

    def determinarVinosActualizar(self):
        pass

    def crearVino(self, vino):
        # Crear un nuevo vino en la bodega seleccionada
        maridaje = self.buscarMaridaje(vino.maridaje)
        varietal = self.buscarTipoUva(vino.varietal.tipoUva)
        vinoNuevo =self.crearVinos(vino, maridaje, varietal)
        vino.bodega.addVino(vinoNuevo)

    def buscarMaridaje(self, maridajeB): #maridajeB es el maridaje que hay que buscar
        for maridaje in self.maridajes:
            if maridaje.sosMaridaje(maridajeB):
                return maridaje
            return None

    def buscarTipoUva(self,tipoUvaB):
        for tipoUva in self.tipoUvas:
            if tipoUva.sosTipoUva(tipoUvaB):
                return tipoUva
            return None
            
    def crearVinos(self,vino, maridaje, varietal):
        nuevoVino = Vino(vino.bodega, vino.nombre, vino.anio, vino.imgEtiqueta, vino.precioARS, maridaje, varietal, vino.notaCata)
        nuevoVino.crearVarietal(varietal.descripcion, varietal.porcentajeUva, varietal.tipoUva)
        return nuevoVino

    def buscarSeguidoresBodega(self, bodegasActualizadas):
        nombresUsuarios = []
        for enofilo in self.enofilos:
            for bodega in bodegasActualizadas:
                if enofilo.seguisABodega(bodega):
                    nombresUsuarios.append(enofilo.getNombreUsuario())

        return nombresUsuarios