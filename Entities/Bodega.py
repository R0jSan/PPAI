import datetime


class Bodega:
    def __init__(self, fechaUltimaActualizacion, region, nombre, periodoActualizacion, historia, descripcion, coordUbi):
        self.fechaUltimaActualizacion = fechaUltimaActualizacion
        self.region = region
        self.nombre = nombre
        self.periodoActualizacion = periodoActualizacion
        self.historia = historia
        self.descripcion = descripcion
        self.coordUbi = coordUbi
        self.vinos = []

    def addVino(self, vino):
        self.vinos.append(vino)

    def mostrarTodosVinos(self):
        for vino in self.vinos:
            vino.mostrarVino(self)

    # Metodos get para cada atributo
    def getDescripcion(self):
        return self.descripcion
    
    def getUbicacion(self):
        return self.ubicacion
    
    def getHistoria(self):
        return self.historia
    
    def getNombre(self):
        return self.nombre
    
    def getPeriodoActualizacion(self):
        return self.periodoActualizacion
    
    def getFechaUltActualizacion(self):
        return self.fechaUltimaActualizacion

    # Métodos set para cada atributo
    def setDescripcion(self, valor):
        self.descripcion = valor

    def setUbicacion(self, valor):
        self.ubicacion = valor

    def setHistoria(self, valor):
        self.historia = valor

    def setNombre(self, valor):
        self.nombre = valor

    def setFechaUltActualizacion(self, valor):
        self.fechaUltimaActualizacion = valor

    def setPeriodoActualizacion(self, valor):
        self.periodoActuaizacion = valor

    def sePuedeActualizarNovedades(self, fechaActual):

     # funcion que retorna true o false si a transcurrido el periodo de actualizacion, toma la fecha actual y compara la diferencia 
     #de meses con el periodo de actualizacion   
        diferencia = fechaActual -  self.fechaUltimaActualizacion
        return self.periodoActualizacion <= (diferencia.days/30)
    
    """
    Funcion tenesEsteVino()
    Recibe como parámetro un objeto de tipo Vino
    self.vino es un atributo de la clase Bodega y contiene un array con todos los vinos de la bodega
    sosEsteVino es un método de la clase Vino y devuelve True en caso de serlo
    """
    def tenesEsteVino(self, vinobusqueda):
        for vino in self.vinos:
            if vino.sosEsteVino(vinobusqueda.nombre):
                return True
        return False

    def actualizarDatosVino(self, vinoActualizar):
        for vino in self.vinos:
            if vino.sosVinoParaActualizar(vinoActualizar):
                vino.setPrecio(vinoActualizar.precioARS)
                vino.setNotaCata(vinoActualizar.notaCata)
                vino.setimgEtiqueta(vinoActualizar.imgEtiqueta)
                vino.setFechaActualizacion(datetime.datetime.now())

    def contarReseñas():
        pass


