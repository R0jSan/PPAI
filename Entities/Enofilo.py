from Entities.Usuario import Usuario

class Enofilo:
    def __init__(self, nombre, apellido, imgPerfil, usuario=Usuario()):
        self.siguiendo = []
        self.nombre = nombre
        self.apellido = apellido
        self.imgPerfil = imgPerfil
        self.usuario = usuario

    def seguisABodega(self, bodega):
        return self.siguiendo.sosDeBodega(bodega)

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
    
    # def getColeccionFavoritos(self):
    #    return self.coleccionFavoritos
    
#Metodos de Pantalla
    def mostrarAmigosSeguidos(self):
        if self.siguiendo:
            print("Amigos seguidos:")
            for amigo in self.siguiendo:
                print(amigo)
        else:
            print("El enofilo no tiene amigos seguidos")
""" 
    def mostrarColeccionFavoritos(self):
        if self.coleccionFavoritos:
            print("Coleccion de Favoritos:")
            for favorito in self.coleccionFavoritos:
                print(favorito)
        else:
            print("El enofilo no tiene ningun vino favorito")
"""