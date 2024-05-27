import datetime
import sys
import random
from PyQt5.QtWidgets import QApplication
from Entities.Bodega import Bodega
from Entities.Vino import Vino
from Interface.PantallaImportacionNovedades import PantallaImportacionNovedades
from Controllers.GestorImportacionNovedades import GestorImportacionNovedades

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
        border-radius: 15px;
        height: 70px;
        width: 350px;
    }
    QPushButton:hover {
        background-color: #8ff8ff
    }
    QListWidget {
        font-size: 15px;
        color: black;
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
    bodegasMock = [
    Bodega(
        fechaUltimaActualizacion=datetime.datetime(2023, 5, 27), 
        region="Cuyo", 
        nombre="Catena Zapata", 
        periodoActualizacion=1, 
        historia="Fundada en 1902, Bodega Catena Zapata es reconocida por su rol pionero en haber hecho resurgir la variedad Malbec y haber descubierto los terroirs de altura extrema al pie de los Andes.", 
        descripcion="Con un edificio principal de estilo maya, esta bodega es famosa por su malbec de gran altitud.", 
        coordUbi="Cobos s/n - Luján de Cuyo (5509), Mendoza, Argentina"
    ),
    Bodega(
        fechaUltimaActualizacion=datetime.datetime(2022, 8, 15), 
        region="Cuyo", 
        nombre="Santa Julia", 
        periodoActualizacion=1, 
        historia="Julia es la única hija de José Zuccardi. Creada en su honor, Santa Julia representa nuestro compromiso para alcanzar los niveles más altos de calidad, mediante prácticas sustentables que contribuyan al cuidado del medio ambiente y siendo útiles para la comunidad en que vivimos.", 
        descripcion="Productora de vinos y aceite de oliva con visitas guiadas, clases de cocina, degustaciones y almuerzo.", 
        coordUbi="Ruta Provincial 33, km 7,5 (M5531) Maipú, Mendoza, Argentina"
    ),
    Bodega(
        fechaUltimaActualizacion=datetime.datetime(2025, 3, 10), 
        region="Cuyo", 
        nombre="La Azul", 
        periodoActualizacion=1, 
        historia="En 2003 nace Bodega La Azul, pero la tradición del cultivo de la viña irriga nuestras venas desde que nuestros abuelos llegaron al Valle de Uco y entendieron que en este suelo pedregoso podrían producirse excelentes frutas.", 
        descripcion="La Azul es una pequeña bodega situada al pie del imponente Cordón del Plata, parte de la Cordillera de Los Andes, en el Valle de Uco, corazón de la provincia de Mendoza.", 
        coordUbi="Caminos del Vino, M5561 Tupungato, Mendoza, Argentina"
    ),
    Bodega(
        fechaUltimaActualizacion=datetime.datetime(2020, 11, 5), 
        region="Cuyo", 
        nombre="Los Toneles", 
        periodoActualizacion=1, 
        historia="Bodega urbana por excelencia. Su arquitectura original es de 1922 y sus espacios encierran encanto e historia. Puesta en valor a principios del 2010, ahora es Patrimonio Cultural Mendocino.", 
        descripcion="Anfitriones por naturaleza, Bodega Los Toneles garantiza excelencia de servicio y máxima calidad de productos logrando experiencias memorables.", 
        coordUbi="Acceso Este, Lateral Norte 1360 Nueva ciudad, Guaymallen"
    )
]
    
    vinosMock = [
    Vino(bodegasMock[0], "Catena Malbec", 2019, "etiqueta_catena_malbec.jpg", 1200),
    Vino(bodegasMock[0], "Catena Chardonnay", 2020, "etiqueta_catena_chardonnay.jpg", 1300),
    Vino(bodegasMock[1], "Santa Julia Malbec", 2018, "etiqueta_santa_julia_malbec.jpg", 900),
    Vino(bodegasMock[1], "Santa Julia Cabernet Sauvignon", 2017, "etiqueta_santa_julia_cabernet.jpg", 1000),
    Vino(bodegasMock[2], "La Azul Malbec", 2016, "etiqueta_la_azul_malbec.jpg", 800),
    Vino(bodegasMock[2], "La Azul Blanco", 2021, "etiqueta_la_azul_blanco.jpg", 750),
    Vino(bodegasMock[3], "Los Toneles Reserva", 2015, "etiqueta_los_toneles_reserva.jpg", 1500),
    Vino(bodegasMock[3], "Los Toneles Gran Reserva", 2014, "etiqueta_los_toneles_gran_reserva.jpg", 2000)
]
    
    for vino in vinosMock:
        vino.bodega.vinos.append(vino)
    
    gestor.bodegas = bodegasMock

    # Mostrar la pantalla y ejecutar el método del gestor
    pantalla.show()
    gestor.opcionImportarActualizacionVinos()

    # Ejecutar el loop de la aplicación
    sys.exit(app.exec_())