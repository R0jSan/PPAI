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

    def mostrarVinos(self):
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

    # 

    def sePuedeActualizarNovedades(self):

     #funcion que retorna true o false si a transcurrido el perriodo de actualizacion, toma la fecha actual y compara la diferencia 
     #de meses con el periodo de actualizacion   
        
        diferencia = datetime.datetime.now() -  self.fechaUltimaActualizacion
        return self.periodoActualizacion <= (diferencia.days/30)
