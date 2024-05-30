from Entities.TipoUva import TipoUva

class Varietal():
    def __init__(self, descripcion, porcentajeUva, tipoUva):
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
    
    def setDescripcion(self, valor):
        self.descripcion = valor

    def setPorcentajeUva(self, valor):
        self.porcentajeUva = valor

    def setTipoUva(self, valor):
        self.tipoUva = valor
        
