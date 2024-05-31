from Entities.Vino import Vino
from Interface.InterfazApiBodega import InterfazApiBodega
from Interface.InterfazNotificacionesPush import InterfazNotificacionesPush
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
        self.seguidores = []
        self.pantallaNotificacion = None

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
    y llama a la funcion obtenerActualizacionBodegaeleccionada(), pasandole como parametro un array
    """
    def tomarBodegasSeleccionada(self):
        # self.bodegaSeleccionPantalla es un array de objetos QListWidgetItem, tengo que aplicarle .text() para filtrar        
        self.bodegaSeleccionPantalla = self.pantallaImportacionNovedades.tomarBodegasSeleccionada()
        bodegasSeleccionadas = []
        # Dos ciclos for para obtener los objetos bodega a partir del nombre tomado desde la pantalla
        for bodegaNombre in self.bodegaSeleccionPantalla:
            for bodega in self.bodegasActualizables:
                if bodegaNombre.text() == bodega.nombre:
                    bodegasSeleccionadas.append(bodega)

        self.obtenerActualizacionBodegaSeleccionada(bodegasSeleccionadas)

    """
    Funcion obtenerActVinosBodegaSeleccionada()
    devuelve un array con lo vinos actualizados que tiene la API
    """
    def obtenerActualizacionBodegaSeleccionada(self, bodegasSeleccionadas):
        actualizaciones =  self.apiBodega.obtenerActualizacionesVinos(bodegasSeleccionadas)
        self.obtenerVinosAActualizar(actualizaciones, bodegasSeleccionadas)
    """
    funcion obtenerVinosActualizables()
    El parametro "actualizacionesVinos" contiene un array con los vinos a modificar
    """
    def obtenerVinosAActualizar(self, actualizacionesVinos, bodegasSeleccionadas):
        for bodega in bodegasSeleccionadas:
            for vino in actualizacionesVinos:
                if bodega.tenesEsteVino(vino): # Modificado
                    self.vinosActualizables.append(vino)
        # Llamado a la funcion actualizarOCrearVinos
        self.actualizarOCrearVinos(bodegasSeleccionadas)


    def actualizarOCrearVinos(self, bodegaSeleccionada):
        for bodega in bodegaSeleccionada:
            for vino in self.vinosActualizables:
                if bodega.tenesEsteVino(vino):
                    self.actualizarCaracteristicasVinoExistente(vino,bodega)
                else:
                    self.crearVino(vino)

        if len(self.vinosActualizables) > 0:
            self.pantallaImportacionNovedades.mostrarVinosActualizados(bodegaSeleccionada, self.vinosActualizables)
            self.pantallaImportacionNovedades.stacked_widget.setCurrentIndex(2)        
            self.enviarNotificacionesPush(bodegaSeleccionada)
        else:
            self.pantallaImportacionNovedades.mostrarVinosActualizados([], [])
            self.pantallaImportacionNovedades.stacked_widget.setCurrentIndex(2)
        self.finCU()     

    def actualizarCaracteristicasVinoExistente(self, vino,bodega):
        bodega.actualizarDatosVino(vino)

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

    def enviarNotificacionesPush(self, bodegas):
        usuarios = self.buscarSeguidoresBodega(bodegas)
        
        for bodega in bodegas:
            self.pantallaNotificacion = InterfazNotificacionesPush(usuarios, bodega)
            self.pantallaNotificacion.notificarNovedadVinoParaBodega()


    def buscarSeguidoresBodega(self, bodegas):
        nombresUsuarios = []
        for enofilo in self.enofilos:
            for bodega in bodegas:
                if enofilo.seguisABodega(bodega):
                    nombresUsuarios.append(enofilo.getNombreUsuario())

        return nombresUsuarios
    
    def finCU(self):
        del self.bodegas
        del self.bodegasActualizables
        del self.nombreBodegasActualizables
        del self.pantallaImportacionNovedades
        del self.maridajes
        del self.tiposUvas
        del self.vinosActualizables
        del self.fechaActual 
        del self.bodegaSeleccionPantalla
        del self.enofilos
        del self.seguidores
        del self.pantallaNotificacion