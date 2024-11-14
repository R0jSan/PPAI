from Entities.Vino import Vino
from Interface.InterfazApiBodega import InterfazApiBodega
from Interface.InterfazNotificacionesPush import InterfazNotificacionesPush
from datetime import datetime
from Interface.ISujeto import ISujeto

class GestorImportacionNovedades(ISujeto):
    apiBodega = InterfazApiBodega() # no se donde iria esto
    def __init__(self, pantallaImportacionNovedades):
        super().__init__()
        self.bodegas = [] # Son todas la bodegas
        self.bodegasActualizables = [] # Son las bodegas que se pueden actualizar
        self.nombreBodegasActualizables = [] # Son el nombre de las bodegas que se pueden actualizar
        self.pantallaImportacionNovedades = pantallaImportacionNovedades # Es la pantalla
        self.maridajes = []
        self.tiposUvas = []
        self.vinosActualizables = {} # Los vinos que se van a actualizar, cambiado a diccionario para que almacene de que bodega es tambien
        self.fechaActual = None # Es la fecha actual calculada por el gestor
        self.bodegaSeleccionPantalla = []
        self.enofilos = []
        self.seguidores = []
        self.pantallaNotificacion = None
        self.observadores = []

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
        self.bodegaSeleccionPantalla = self.pantallaImportacionNovedades.tomarBodegasSeleccionada()
        bodegasSeleccionadas = []
        # Dos ciclos for para obtener los objetos bodega a partir del nombre tomado desde la pantalla
        if self.bodegaSeleccionPantalla is not None:
            for bodegaNombre in self.bodegaSeleccionPantalla:  # bodegaNombre ahora es un string
                for bodega in self.bodegasActualizables:
                    if bodegaNombre == bodega.nombre:  # Se compara directamente con el nombre de la bodega
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
        self.vinosActualizables.clear()
        for bodega in bodegasSeleccionadas:
            vinos_para_bodega = []
            for vino in actualizacionesVinos:
                if bodega.tenesEsteVino(vino): # Modificado
                    vinos_para_bodega.append(vino)
            if vinos_para_bodega:
                self.vinosActualizables[bodega] = vinos_para_bodega
            # Llamado a la funcion actualizarOCrearVinos
        self.actualizarOCrearVinos()

    """
    funcion actualizarOCrearVinos()
    Se le pasa la/las bodega seleccionada y va viendo si los vinos de cada bodega
    tuvieron una actualizacion y en caso de que el vino no existe lo crea.
    Cuando lo actualiza muestra por panatalla la infromacion de los vinos actualizados
    y procede a enviar las notificaciones push a todos los enofilos que siguen a esa bodega
    """
    def actualizarOCrearVinos(self):
        for bodega,vinos in self.vinosActualizables.items():
            for vino in vinos:
                if bodega.tenesEsteVino(vino):
                    self.actualizarCaracteristicasVinoExistente(vino,bodega)
                else:
                    self.crearVino(vino, bodega)

        if len(self.vinosActualizables) > 0:
            bodegasSeleccionadas = list(self.vinosActualizables.keys())
            self.pantallaImportacionNovedades.mostrarVinosActualizados(self.vinosActualizables)
            self.pantallaImportacionNovedades.stacked_widget.setCurrentIndex(2)        
            self.enviarNotificacionesPush(bodegasSeleccionadas)
        else:
            self.pantallaImportacionNovedades.mostrarVinosActualizados([], [])
            self.pantallaImportacionNovedades.stacked_widget.setCurrentIndex(2)
        self.finCU()     

    def actualizarCaracteristicasVinoExistente(self, vino,bodega):
        bodega.actualizarDatosVino(vino)

    def crearVino(self, vino_data, bodega):
        nuevo_vino = Vino(
            bodega, vino_data.nombre, vino_data.aniada,
            vino_data.imgEtiqueta, vino_data.precioARS,
            vino_data.notaCata
        )

        nuevo_vino.maridaje = self.buscarMaridaje(vino_data.maridaje)

        # Asignar todos los varietales al nuevo vino
        for varietal in vino_data.varietales:
            nuevo_vino.agregarVarietal(
                varietal.getDescripcion(),
                varietal.getPorcentajeUva(),
                varietal.getTipoUva()
            )

        bodega.addVino(nuevo_vino)

    def buscarMaridaje(self, maridajeB): #maridajeB es el maridaje que hay que buscar
        for maridaje in self.maridajes:
            if maridaje.sosMaridaje(maridajeB):
                return maridaje
            return None
            

    """
    funcion enviarNotificacionesPush
    Crea la interfaz de notificaciones push y la suscribe a la lista de observadores
    del gestor. Luego busca a los enofilos que siguen a la bodega actualizada y los notifica.
    
    """
    def enviarNotificacionesPush(self, bodegas):
        notificadorPush = InterfazNotificacionesPush()
        self.suscribir(notificadorPush)

        # Para cada bodega seleccionada, buscar los seguidores y envia la notificación correspondiente
        for bodega in bodegas:
            usuarios_seguidores = self.buscarSeguidoresBodega([bodega])
            self.notificar(bodega, usuarios_seguidores)

    def buscarSeguidoresBodega(self, bodegas):
        nombresUsuarios = []
        for enofilo in self.enofilos:
            for bodega in bodegas:
                if enofilo.seguisABodega(bodega):
                    nombresUsuarios.append(enofilo.getNombreUsuario())


        return nombresUsuarios
    
    def suscribir(self, observer):
        if observer not in self.observadores:
            self.observadores.append(observer)

    def quitar(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificar(self,bodega, usuarios):
        for observador in self.observadores:
            observador.actualizar(usuarios, bodega.nombre)
        

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
