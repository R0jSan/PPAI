class Siguiendo:
    def __init__(self, bodega, fechaInicio):
        self.bodega = bodega
        self.fechaFin = None
        self.fechaInicio = fechaInicio

    def sosDeBodega(self, bodegaComparar):
        return self.bodega == bodegaComparar

    
    def setFechaFin(self,fechaFin):
        self.fechaFin = fechaFin

    def getfechaInicio(self):
        return self.fechaInicio

    def getfechaFin(self):
        return self.fechaFin
