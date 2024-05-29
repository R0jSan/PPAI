from Interface.style import styles
from PyQt5.QtGui import  QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import *

class PantallaImportacionNovedades(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú de administrador de Bodegas")
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
        volver_button = QPushButton("Volver")

        widgets = [bon_vino_label, menu_importar_label, bodegas_actualizables_label, self.bodegas_actualizables_list, self.seleccionar_bodega_button, volver_button]

        styles.alinear(bon_vino_label, styles.TITLE_SIZE)
        styles.alinear(menu_importar_label, styles.LABEL_SIZE)
        styles.alinear(bodegas_actualizables_label, styles.LABEL_SIZE)

        styles.crearLayout(widgets, layout)

        self.seleccionar_bodega_button.clicked.connect(self.tomarBodegasSeleccionada)
        volver_button.clicked.connect(self.mostrarVentanaMenuPrincipal)
        return widget

    def ventanaBodegaSeleccionada(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        bon_vino_label = QLabel("BON VINO")
        self.bodega_label = QLabel()
        vinos_actualizados_label = QLabel("Vinos actualizados: ")
        lista_vinos = QListWidget()
        volver_button = QPushButton("Volver")
        widgets = [bon_vino_label, self.bodega_label, vinos_actualizados_label, lista_vinos, volver_button]

        styles.alinear(bon_vino_label, styles.TITLE_SIZE)
        styles.alinear(self.bodega_label, styles.LABEL_SIZE)
        styles.alinear(vinos_actualizados_label, styles.LABEL_SIZE)

        styles.crearLayout(widgets, layout)    

        volver_button.clicked.connect(self.mostrarVentanaImportacionVinos)
        return widget

    def tomarBodegasSeleccionada(self):  
        selectedItems = self.bodegas_actualizables_list.selectedItems()
        if not selectedItems:
            styles.crearBox("Error", "Seleccione una bodega")
        self.bodega_label.setText(f"Bodega {selectedItems[0].text()}")
        self.mostrarVentanaBodegaSeleccionada()
        return selectedItems
            
    def mostrarBodegasActualizables(self, bodegas):
        self.bodegas_actualizables_list.clear()
        self.bodegas_actualizables_list.addItems(bodegas)

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
