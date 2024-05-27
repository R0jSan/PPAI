from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import *

class PantallaImportacionNovedades(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú de administrador de Bodegas")
        self.setFixedSize(390, 695) 

        # Imagen de fondo
        pixmap = QPixmap('bonvino.png')
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)

        # Ventana principal (menu)
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)
        
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Crea las ventanas "menu principal" y "importacion de vinos"
        self.menu_principal_widget = self.menu_principal_widget()
        self.importacion_vinos_widget = self.importacion_vinos_widget()
        self.bodega_seleccionada_widget = self.bodega_seleccionada_widget()

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

        bon_vino_label.setFont(QFont("PMingLiU-ExtB", 50))
        bon_vino_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        
        main_menu_label.setFont(QFont("PMingLiU-ExtB", 15))
        main_menu_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        layout.addWidget(bon_vino_label)
        layout.addWidget(main_menu_label)

        layout_botones = QVBoxLayout()
        layout_botones.addWidget(importar_vinos_button)
        layout_botones.addWidget(placeholder1_button)
        layout_botones.addWidget(placeholder2_button)

        layout.addLayout(layout_botones)
        layout.setSpacing(25)
        
        importar_vinos_button.clicked.connect(self.mostrar_importacion_vinos)

        widget.setLayout(layout)
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


        bon_vino_label.setFont(QFont("PMingLiU-ExtB", 50))
        bon_vino_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        menu_importar_label.setFont(QFont("PMingLiU-ExtB", 15))
        menu_importar_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        bodegas_actualizables_label.setFont(QFont("PMingLiU-ExtB", 15))
        bodegas_actualizables_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        layout.addWidget(bon_vino_label)
        layout.addWidget(menu_importar_label)
        layout.addWidget(bodegas_actualizables_label)
        layout.addWidget(self.bodegas_actualizables_list)
        layout.addWidget(self.seleccionar_bodega_button)
        layout.addWidget(volver_button)

        self.seleccionar_bodega_button.clicked.connect(self.tomarBodegasSeleccionada)
        volver_button.clicked.connect(self.mostrar_menu_principal)

        widget.setLayout(layout)
        return widget

    def bodega_seleccionada_widget(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        bon_vino_label = QLabel("BON VINO")
        self.bodega_label = QLabel()
        vinos_actualizados_label = QLabel("Vinos actualizados: ")
        lista_vinos = QListWidget()
        volver_button = QPushButton("Volver")

        bon_vino_label.setFont(QFont("PMingLiU-ExtB", 50))
        bon_vino_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.bodega_label.setFont(QFont("PMingLiU-ExtB", 15))
        self.bodega_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        vinos_actualizados_label.setFont(QFont("PMingLiU-ExtB", 15))
        self.bodega_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        layout.addWidget(bon_vino_label)
        layout.addWidget(self.bodega_label)
        layout.addWidget(vinos_actualizados_label)
        layout.addWidget(lista_vinos)
        layout.addWidget(volver_button)

        volver_button.clicked.connect(self.mostrar_importacion_vinos)

        return widget

    def tomarBodegasSeleccionada(self):  
        selectedItems = self.bodegas_actualizables_list.selectedItems()
        if selectedItems:
            self.bodega_label.setText(f"Bodega {selectedItems[0].text()}")
            bodegaseleccionada = selectedItems
            self.stacked_widget.setCurrentIndex(2)
            return bodegaseleccionada
        else:
            adv = QMessageBox()
            adv.setWindowTitle("Error")
            adv.setText("Seleccione una bodega")
            stylesheet_adv = '''
                            QLabel { 
                                color: black; 
                                }
                            QPushButton {
                                font-size: 15px; 
                                background-color: white; 
                                color: black; 
                                border-radius: 2px; 
                                height: 25px; 
                                width: 160px; 
                                }
                            QPushButton:hover {
                                background-color: #8ff8ff
                                }'''
            adv.setStyleSheet(stylesheet_adv)
            adv.exec_()
            
    def mostrarBodegasActualizables(self, bodegas):
        self.bodegas_actualizables_list.clear()
        self.bodegas_actualizables_list.addItems(bodegas)

    def mostrar_importacion_vinos(self):
        self.stacked_widget.setCurrentIndex(1) 

    def mostrar_menu_principal(self):
        self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PantallaImportacionNovedades()
    window.show()
    sys.exit(app.exec_())

stylesheet = """
    QLabel {
        background-color: transparent;
        color: black;
        padding: 5px;
    }
    QPushButton {
        font-size: 20px;
        background-color: white;
        color: black;
        border-radius: 30px;
        height: 70px;
        width: 350px;
    }
    QPushButton:hover {
        background-color: #8ff8ff
    }
    QListWidget {
        
    }
    }
"""