from notifypy import Notify


class InterfazNotificacionesPush:
    def __init__(self, usuarios, bodega):
        self.usuariosNombres = usuarios
        self.bodega = bodega

    def notificarNovedadVinoParaBodega(self):
        notificacion = Notify()
        for usuario in self.usuariosNombres:
            notificacion.title = f"{self.bodega.nombre}"
            notificacion.message = f"Hola {usuario}, no te pierdas las novedades!!!"
            notificacion.application_name = "BONVINO"
            notificacion.icon = "Media\\icons\\icono_notificacion.png"
            notificacion.send()