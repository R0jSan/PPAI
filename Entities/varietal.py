from TipoUva import TipoUva

class Varietal():
    def __init__(self, descripcion=str(), porcentajeUva=float(), tipoUva=TipoUva('','')):
        self.descripcion = descripcion
        self.porcentajeUva = porcentajeUva
        self.tipoUva = tipoUva
    
    def conocerTipoUva(self):
        return f"{self.tipoUva.getNombre()} - {self.tipoUva.getDescripcion()}"
    
    def esDeUva(self,uva=str()):
        return self.tipoUva.sosTipoUva(uva)
    #get

    def getDescripcion(self):
        return self.descripcion
    
    def getPorcentajeUva(self):
        return self.porcentajeUva
    
    def getTipoUva(self):
        return self.tipoUva
    
    #set
    
    def setDescripcion(self, valor=str()):
        self.descripcion = valor

    def setPorcentajeUva(self, valor=float()):
        self.porcentajeUva = valor

    def setTipoUva(self, valor=TipoUva('','')):
        self.tipoUva = valor
        