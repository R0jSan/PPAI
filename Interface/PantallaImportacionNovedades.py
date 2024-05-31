from Interface.style import styles
from PyQt5.QtGui import  QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import *
from Controllers.GestorImportacionNovedades import GestorImportacionNovedades
class PantallaImportacionNovedades(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú de administrador de Bonvino")
        self.setFixedSize(390, 695) 

        # Imagen de fondo
        self.definir_fondo("Interface\\style\\bonvino.png")

        # Ventana principal
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Crea las ventanas "menu principal", "importacion de vinos" y "bodega seleccionada"
        self.menu_principal_widget = self.ventanaMenuPrincipal()
        self.importacion_vinos_widget = self.ventanaImportacionVinos()
        self.bodega_seleccionada_widget = self.ventanaBodegaSeleccionada()

        # Añade cada ventana a la "pila"
        self.stacked_widget.addWidget(self.menu_principal_widget)
        self.stacked_widget.addWidget(self.importacion_vinos_widget)
        self.stacked_widget.addWidget(self.bodega_seleccionada_widget)

        self.stacked_widget.setCurrentIndex(0)  #Las "ventanas" son capas apiladas, la 0 es el menu principal 

    def ventanaMenuPrincipal(self):
        # Layout del menu principal
        widget = QWidget()
        layout = QVBoxLayout(widget)

        bon_vino_label = QLabel("BON VINO")
        main_menu_label = QLabel("- Menú Administrador de Bodegas -")
        importar_vinos_button = QPushButton("Importar Actualización de Vinos")
        placeholder1_button = QPushButton("-")
        placeholder2_button = QPushButton("-")

        widgets = [bon_vino_label, main_menu_label, importar_vinos_button, placeholder1_button, placeholder2_button]

        styles.alinear(bon_vino_label, styles.TITLE_SIZE)
        styles.alinear(main_menu_label, styles.LABEL_SIZE)

        styles.crearLayout(widgets, layout)

        importar_vinos_button.clicked.connect(self.mostrarVentanaImportacionVinos)
        return widget

    def ventanaImportacionVinos(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        bon_vino_label = QLabel("BON VINO")
        menu_importar_label = QLabel("Menu Importar Actualización de Vinos")
        bodegas_actualizables_label = QLabel("Bodegas con actualizaciones pendientes:")
        self.bodegas_actualizables_list = QListWidget()
        self.seleccionar_bodega_button = QPushButton("Seleccionar Bodega")
        # volver_button = QPushButton("Volver")

        widgets = [bon_vino_label, menu_importar_label, bodegas_actualizables_label, self.bodegas_actualizables_list, self.seleccionar_bodega_button] # , volver_button

        styles.alinear(bon_vino_label, styles.TITLE_SIZE)
        styles.alinear(menu_importar_label, styles.LABEL_SIZE)
        styles.alinear(bodegas_actualizables_label, styles.LABEL_SIZE)

        styles.crearLayout(widgets, layout)

        self.seleccionar_bodega_button.clicked.connect(self.tomarBodegasSeleccionada)
        # volver_button.clicked.connect(self.mostrarVentanaMenuPrincipal)
        return widget

    def ventanaBodegaSeleccionada(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        bon_vino_label = QLabel("BON VINO")
        self.bodega_label = QLabel()
        vinos_actualizados_label = QLabel("Vinos actualizados: ")
        self.lista_vinos = QListWidget()
        #volver_button = QPushButton("Volver")
        widgets = [bon_vino_label, self.bodega_label, vinos_actualizados_label, self.lista_vinos] # , volver_button

        styles.alinear(bon_vino_label, styles.TITLE_SIZE)
        styles.alinear(self.bodega_label, styles.LABEL_SIZE)
        styles.alinear(vinos_actualizados_label, styles.LABEL_SIZE)

        styles.crearLayout(widgets, layout)    

        #volver_button.clicked.connect(self.mostrarVentanaImportacionVinos)
        return widget


    """
    Funcion tomarBodegasSeleccionada() devuelve un array con objetos QListWidgetItem
    Al aplicarle .text() a cada objeto voy a obtener el nombre de la bodega y así buscar las seleccionadas en el gestor
    """
    def tomarBodegasSeleccionada(self):  
        selectedItems = self.bodegas_actualizables_list.selectedItems()
        if selectedItems:
            for item in selectedItems:
            # self.bodega_label.setText(f"Bodega {selectedItems[0].text()}")
            # self.mostrarVentanaBodegaSeleccionada()
                bodegasSeleccionadas = []
                bodegasSeleccionadas.append(item)

            # return selectedItems[0]
            # return selectedItems[0].text() # Agregado
            return bodegasSeleccionadas
        else:
            styles.crearBox("Error", "Seleccione una bodega")

    """
    funcion mostrarBodegasActualizables()
    Recibe como parametro las bodegas que tienen actualizaciones disponibles.
    El parametro bodegas es un array
    """      
    def mostrarBodegasActualizables(self, bodegas):
        msj = bodegas
        self.bodegas_actualizables_list.clear()
        if len(bodegas) == 0:
            msj = ["No hay bodegas en período de actualización"]
        self.bodegas_actualizables_list.addItems(msj)

    def mostrarVentanaMenuPrincipal(self):
        self.stacked_widget.setCurrentIndex(0)

    def mostrarVentanaImportacionVinos(self):
        self.stacked_widget.setCurrentIndex(1)
    
    def mostrarVentanaBodegaSeleccionada(self):
        self.stacked_widget.setCurrentIndex(2)

    def definir_fondo(self, img):
        pixmap = QPixmap(img)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)

    def mostrarVinosActualizados(self, bodegas, vinos):
        if len(vinos) > 0:
            # print(f"vinos: {len(vinos)} - bodegas: {len(bodegas)}")
            for bodega in bodegas:
                
                self.bodega_label.setText(f"Bodega: {bodega.getNombre()}")
                self.lista_vinos.clear()
    
                for vino in vinos:
                    if bodega.getNombre() == vino.bodega:
                        vino_widget = QWidget()
                        vino_layout = QVBoxLayout(vino_widget)
            
                        nombre_label = QLabel(f"Nombre: {vino.nombre}")
                        anio_label = QLabel(f"Aniada: {vino.aniada}")
                        precio_label = QLabel(f"Precio: {vino.precioARS} ARS")
                        nota_cata_label = QLabel(f"Nota de cata: {vino.notaCata}")
            
                        nombre_label.setStyleSheet("font-weight: bold; color: #333;")
                        anio_label.setStyleSheet("color: #555;")
                        precio_label.setStyleSheet("color: #555;")
                        nota_cata_label.setStyleSheet("color: #555;")
            
                        vino_layout.addWidget(nombre_label)
                        vino_layout.addWidget(anio_label)
                        vino_layout.addWidget(precio_label)
                        vino_layout.addWidget(nota_cata_label)
                        vino_layout.setContentsMargins(10, 10, 10, 10)
                        vino_layout.setSpacing(5)
            
                        list_item = QListWidgetItem(self.lista_vinos)
                        list_item.setSizeHint(vino_widget.sizeHint())
            
                        self.lista_vinos.addItem(list_item)
                        self.lista_vinos.setItemWidget(list_item, vino_widget)
        else:
            
            vino_widget = QWidget()
            vino_layout = QVBoxLayout(vino_widget)
            nombre_label = QLabel(f"No hay actualizaciones disponibles")
            nombre_label.setStyleSheet("font-weight: bold; color: #333;")
            vino_layout.addWidget(nombre_label)
            list_item = QListWidgetItem(self.lista_vinos)
            list_item.setSizeHint(vino_widget.sizeHint())
            self.lista_vinos.addItem(list_item)
            self.lista_vinos.setItemWidget(list_item, vino_widget)