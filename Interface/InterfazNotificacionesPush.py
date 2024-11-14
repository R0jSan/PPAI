from notifypy import Notify

from Interface.IObserver import IObserver


class InterfazNotificacionesPush(IObserver):
    def __init__(self):
        super().__init__()
        self.usuarios = []  
        self.bodega = ""

    def actualizar(self, usuarios, bodega):
        self.usuarios = usuarios
        self.nombreBodega = bodega

        self.generarNotificaciones()

    def generarNotificaciones(self):
        """
        Genera y envía notificaciones a todos los usuarios suscritos.
        """
        for usuario in self.usuarios:
            self.enviarNotificacion(usuario)

    def enviarNotificacion(self, usuario):
        notificacion = Notify()
        notificacion.title = f"Bodega {self.nombreBodega}"
        notificacion.message = f"Hola {usuario}, no te pierdas las novedades!!!"
        notificacion.application_name = "BONVINO"
        notificacion.icon = "Media\\icons\\icono_notificacion.png"
        notificacion.send()
