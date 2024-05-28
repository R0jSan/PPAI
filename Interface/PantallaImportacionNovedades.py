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
        self.menu_principal_widget = self.menu_principal_widget()
        self.importacion_vinos_widget = self.importacion_vinos_widget()
        self.bodega_seleccionada_widget = self.bodega_seleccionada_widget()

        # Añade cada ventana a la "pila"
        self.stacked_widget.addWidget(self.menu_principal_widget)
        self.stacked_widget.addWidget(self.importacion_vinos_widget)
        self.stacked_widget.addWidget(self.bodega_seleccionada_widget)

        self.stacked_widget.setCurrentIndex(0)  #Las "ventanas" son capas apiladas, la 0 es el menu principal 

    def menu_principal_widget(self):
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

        styles.crearlayout(widgets, layout)

        importar_vinos_button.clicked.connect(self.mostrar_importacion_vinos)
        return widget

    def importacion_vinos_widget(self):
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

        styles.crearlayout(widgets, layout)

        self.seleccionar_bodega_button.clicked.connect(self.tomarBodegasSeleccionada)
        volver_button.clicked.connect(self.mostrar_menu_principal)
        return widget

    def bodega_seleccionada_widget(self):
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

        styles.crearlayout(widgets, layout)    

        volver_button.clicked.connect(self.mostrar_importacion_vinos)
        return widget

    def tomarBodegasSeleccionada(self):  
        selectedItems = self.bodegas_actualizables_list.selectedItems()
        if selectedItems:
            self.bodega_label.setText(f"Bodega {selectedItems[0].text()}")
            # bodegaseleccionada = selectedItems
            self.stacked_widget.setCurrentIndex(2)
        else:
            styles.crear_error_box("Error", "Seleccione una bodega")
            
    def mostrarBodegasActualizables(self, bodegas):
        self.bodegas_actualizables_list.clear()
        self.bodegas_actualizables_list.addItems(bodegas)

    def mostrar_importacion_vinos(self):
        self.stacked_widget.setCurrentIndex(1) 

    def mostrar_menu_principal(self):
        self.stacked_widget.setCurrentIndex(0)

    def definir_fondo(self, img):
        pixmap = QPixmap(img)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(styles.stylesheet_global)
    window = PantallaImportacionNovedades()
    window.show()
    sys.exit(app.exec_())
