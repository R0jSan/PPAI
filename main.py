import sys
import random
from PyQt5.QtWidgets import QApplication
from Interface.PantallaImportacionNovedades import PantallaImportacionNovedades
from Controllers.GestorImportacionNovedades import GestorImportacionNovedades

class MockBodega:
    def __init__(self, nombre, se_puede_actualizar):
        self.nombre = nombre
        self.se_puede_actualizar = se_puede_actualizar

    def sePuedeActualizarNovedades(self):
        return self.se_puede_actualizar

    def getNombre(self):
        return self.nombre

stylesheet = """
    QLabel {
        background-color: transparent;
        color: white;
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

if __name__ == '__main__':
    # Crear una instancia de QApplication antes de cualquier widget
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    pantalla = PantallaImportacionNovedades()
    gestor = GestorImportacionNovedades(pantalla)
    
    # Simular algunas bodegas
    gestor.bodegas = []

    for i in range(20):
        bodega = MockBodega("Nombre Bodega" + str(i), random.choice([True, False]))
        gestor.bodegas.append(bodega)

    # Mostrar la pantalla y ejecutar el método del gestor
    pantalla.show()
    gestor.opcionImportarActualizacionVinos()

    # Ejecutar el loop de la aplicación
    sys.exit(app.exec_())