class Vino:
    def __init__(self, bodega, nombre, anio, imgEtiqueta, precioARS, maridaje, varietal, notaCata):
        self.bodega = bodega
        self.nombre = nombre
        self.anio = anio
        self.imgEtiqueta = imgEtiqueta #!
        self.precioARS = precioARS
        self.maridaje = maridaje
        self.varietal = varietal
        self.fechaActualizacion = None #!
        self.paraActualizar = False #!
        self.notaCata = notaCata

    def crearVino():
        pass

    def crearVarietal():
        pass

    def sosDeBodega(self, bodegaComparar):
        return self.bodega == bodegaComparar

    def sosEsteVino(self, nombreBusqueda):
        return self.nombre == nombreBusqueda

    def sosVinoParaActualizar(self, vinoActualizar):
        return (vinoActualizar.nombre == self.vino)

    def setPrecio(self, nuevoPrecio):
        self.precioARS = nuevoPrecio

    def setimgEtiqueta(self, nuevaImg):
        self.imgEtiqueta = nuevaImg

    def setFechaActualiz(self, nuevaFecha):
        self.fechaActualizacion = nuevaFecha

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