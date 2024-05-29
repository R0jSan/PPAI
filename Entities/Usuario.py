class Usuario:
    def __init__(self, nombre=str(), contraseña=str(), premium=False):
        self.nombre = nombre
        self.contraseña = contraseña
        self.premium = premium
    
    def esPremium(self):
        return self.premium
    
    def mostrarNombre(self):
        return self.nombre
    
    def esTuUsuario(self,nombre):
        return self.nombre == nombre
    
    def getNombre(self):
        return self.nombre