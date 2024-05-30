from Entities.Usuario import Usuario

class Enofilo:
    def __init__(self, nombre, apellido, imgPerfil, usuario=Usuario()):
        self.siguiendo = []
        self.nombre = nombre
        self.apellido = apellido
        self.imgPerfil = imgPerfil
        self.usuario = usuario

    def seguisABodega(self, bodega):
        for i in range(len(self.siguiendo)):
            if self.siguiendo[i].sosDeBodega(bodega):
                return True 

    def getNombreUsuario(self):
        return self.usuario.getNombre()
    
    # Métodos set
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setImagenPerfil(self, imagen):
        self.imgPerfil = imagen
    
    def getApellido(self):
        return self.apellido
    
    def getNombre(self):
        return self.nombre
    
    def getImagenPerfil(self):
        return self.imgPerfil

    def getSiguiendo(self):
        return self.siguiendo
    