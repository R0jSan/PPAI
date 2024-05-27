class TipoUva:
    def __init__(self, nombre=str(), descripcion=str()):
        self.nombre = nombre
        self.descripcion = descripcion

    def sosTipoUva(self, busqueda):
        return self.nombre == busqueda
    
    #get

    def getDescripcion(self):
        return self.descripcion
    
    def getNombre(self):
        return self.nombre
    
    #set
    
    def setDescripcion(self, valor=str()):
        self.descripcion = valor

    def setNombre(self, valor=str()):
        self.nombre = valor
        