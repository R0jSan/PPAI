from Entities.Varietal import Varietal


class Vino:
    def __init__(self, bodega, nombre, aniada, imgEtiqueta, precioARS, maridaje, descripcion, porcentajeUva, tipoUva, notaCata):
        self.bodega = bodega 
        self.nombre = nombre 
        self.aniada = aniada
        self.imgEtiqueta = imgEtiqueta
        self.precioARS = precioARS
        self.maridaje = maridaje
        self.varietal = self.crearVarietal(descripcion,porcentajeUva,tipoUva)
        self.fechaActualizacion = None
        self.notaCata = notaCata

    def crearVarietal(self, descripcion, porcentajeUva, tipoUva):
        nuevo_varietal = Varietal(descripcion, porcentajeUva, tipoUva)
        self.varietal = nuevo_varietal

    def sosDeBodega(self, bodegaComparar):
        return self.bodega == bodegaComparar

    def sosEsteVino(self, nombreBusqueda):
        return self.nombre == nombreBusqueda

    def sosVinoParaActualizar(self, vinoActualizar):
        return (vinoActualizar.nombre == self.nombre)

    def setPrecio(self, nuevoPrecio):
        self.precioARS = nuevoPrecio

    def setimgEtiqueta(self, nuevaImg):
        self.imgEtiqueta = nuevaImg

    def setFechaActualizacion(self, nuevaFecha):
        self.fechaActualizacion = nuevaFecha

    def setNotaCata(self, nuevaNotaCata):
        self.notaCata = nuevaNotaCata

    """
    def mostrarVino(self, bodega):
        print('Nombre: ' + str(self.nombre)
              + '\nAño: ' + str(self.anio)
              + '\nEtiqueta: ' + str(self.imgEtiqueta)
              + '\nPrecio: ' + str(self.precioARS)
              + '\nBodega: ' + str(bodega.nombre)
              + '\nRegión: ' + str(bodega.region)
              + '\n' +'-'*80)
    """