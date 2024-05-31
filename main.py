import datetime
import sys
from PyQt5.QtWidgets import QApplication
from Entities.Bodega import Bodega
from Entities.Maridaje import Maridaje
from Entities.TipoUva import TipoUva
from Entities.Vino import Vino
from Entities.Varietal import Varietal
from Entities.Usuario import Usuario
from Entities.Enofilo import Enofilo
from Entities.Siguiendo import Siguiendo
from Interface.PantallaImportacionNovedades import PantallaImportacionNovedades
from Interface.style import styles
from Controllers.GestorImportacionNovedades import GestorImportacionNovedades

if __name__ == '__main__':
    # Crear una instancia de QApplication antes de cualquier widget
    app = QApplication(sys.argv)
    app.setStyleSheet(styles.stylesheet_global)
    pantalla = PantallaImportacionNovedades()
    # Al gestor le asigna la variable pantalla
    gestor = GestorImportacionNovedades(pantalla)
    
    # Simular algunas bodegas
    bodegasMock = [
    Bodega(
        fechaUltimaActualizacion=datetime.datetime(2023, 5, 27), 
        #fechaUltimaActualizacion = datetime.datetime.now(),
        region="Cuyo", 
        nombre="Catena Zapata", 
        periodoActualizacion=1, 
        historia="Fundada en 1902, Bodega Catena Zapata es reconocida por su rol pionero en haber hecho resurgir la variedad Malbec y haber descubierto los terroirs de altura extrema al pie de los Andes.", 
        descripcion="Con un edificio principal de estilo maya, esta bodega es famosa por su malbec de gran altitud.", 
        coordUbi="Cobos s/n - Luján de Cuyo (5509), Mendoza, Argentina"
    ),
    Bodega(
        fechaUltimaActualizacion=datetime.datetime(2022, 8, 15), 
        #fechaUltimaActualizacion = datetime.datetime.now(),
        region="Cuyo", 
        nombre="Santa Julia", 
        periodoActualizacion=1, 
        historia="Julia es la única hija de José Zuccardi. Creada en su honor, Santa Julia representa nuestro compromiso para alcanzar los niveles más altos de calidad, mediante prácticas sustentables que contribuyan al cuidado del medio ambiente y siendo útiles para la comunidad en que vivimos.", 
        descripcion="Productora de vinos y aceite de oliva con visitas guiadas, clases de cocina, degustaciones y almuerzo.", 
        coordUbi="Ruta Provincial 33, km 7,5 (M5531) Maipú, Mendoza, Argentina"
    ),
    Bodega(
        fechaUltimaActualizacion=datetime.datetime(2025, 3, 10),
        #fechaUltimaActualizacion = datetime.datetime.now(),
        region="Cuyo", 
        nombre="La Azul", 
        periodoActualizacion=1, 
        historia="En 2003 nace Bodega La Azul, pero la tradición del cultivo de la viña irriga nuestras venas desde que nuestros abuelos llegaron al Valle de Uco y entendieron que en este suelo pedregoso podrían producirse excelentes frutas.", 
        descripcion="La Azul es una pequeña bodega situada al pie del imponente Cordón del Plata, parte de la Cordillera de Los Andes, en el Valle de Uco, corazón de la provincia de Mendoza.", 
        coordUbi="Caminos del Vino, M5561 Tupungato, Mendoza, Argentina"
    ),
    Bodega(
        fechaUltimaActualizacion=datetime.datetime(2020, 11, 5), 
        #fechaUltimaActualizacion = datetime.datetime.now(),
        region="Cuyo", 
        nombre="Los Toneles", 
        periodoActualizacion=1, 
        historia="Bodega urbana por excelencia. Su arquitectura original es de 1922 y sus espacios encierran encanto e historia. Puesta en valor a principios del 2010, ahora es Patrimonio Cultural Mendocino.", 
        descripcion="Anfitriones por naturaleza, Bodega Los Toneles garantiza excelencia de servicio y máxima calidad de productos logrando experiencias memorables.", 
        coordUbi="Acceso Este, Lateral Norte 1360 Nueva ciudad, Guaymallen"
    )
]
    
    tiposUva = [
    TipoUva("Malbec", "Una uva roja de origen francés, famosa en Argentina."),
    TipoUva("Cabernet Sauvignon", "Una uva roja ampliamente cultivada en todo el mundo."),
    TipoUva("Chardonnay", "Una uva blanca muy popular utilizada en la producción de vinos espumosos y blancos."),
    TipoUva("Sauvignon Blanc", "Una uva blanca conocida por su alta acidez y aromas herbáceos."),
    TipoUva("Syrah", "Una uva roja que produce vinos oscuros y ricos en sabor."),
]
    
    varietales = [
    Varietal("Varietal 100% Malbec", 100, tiposUva[0]),
    Varietal("Varietal 80% Cabernet Sauvignon, 20% Merlot", 80, tiposUva[1]),
    Varietal("Varietal 100% Chardonnay", 100, tiposUva[2]),
    Varietal("Varietal 90% Sauvignon Blanc, 10% Semillon", 90, tiposUva[3]),
    Varietal("Varietal 75% Syrah, 25% Grenache", 75, tiposUva[4]),
]
    
    maridajes = [
    Maridaje("Carne Roja", "Perfecto para acompañar con Malbec o Cabernet Sauvignon."),
    Maridaje("Pescado", "Ideal para maridar con Sauvignon Blanc o Chardonnay."),
    Maridaje("Quesos", "Combina bien con una amplia variedad de vinos, especialmente Syrah y Chardonnay."),
    Maridaje("Postres", "Marida excelente con vinos dulces y espumosos."),
    Maridaje("Pasta", "Se recomienda acompañar con un buen Merlot o un Cabernet Sauvignon."),
]


    vinosMock = [
    Vino(bodegasMock[0], "Catena Malbec", 2019, "etiqueta_catena_malbec.jpg", 8000, maridajes[0], varietales[0], "Frutado con notas de ciruela y moras."),
    Vino(bodegasMock[0], "Catena Chardonnay", 2020, "etiqueta_catena_chardonnay.jpg", 7600, maridajes[1], varietales[2], "Aromas de manzana verde y pera con un toque de vainilla."),
    Vino(bodegasMock[1], "Santa Julia Malbec", 2018, "etiqueta_santa_julia_malbec.jpg", 8300, maridajes[0], varietales[0], "Notas de frutos rojos y taninos suaves."),
    Vino(bodegasMock[1], "Santa Julia Cabernet Sauvignon", 2017, "etiqueta_santa_julia_cabernet.jpg", 9000, maridajes[4], varietales[1], "Aromas a pimiento verde y grosella negra."),
    Vino(bodegasMock[2], "La Azul Malbec", 2016, "etiqueta_la_azul_malbec.jpg", 6500, maridajes[2], varietales[0], "Sabores intensos de ciruela y especias."),
    Vino(bodegasMock[2], "La Azul Blanco", 2021, "etiqueta_la_azul_blanco.jpg", 7750, maridajes[1], varietales[3], "Fresco con notas cítricas y florales."),
    Vino(bodegasMock[3], "Los Toneles Reserva", 2015, "etiqueta_los_toneles_reserva.jpg", 7500, maridajes[2], varietales[4], "Cuerpo robusto con sabores de roble y frutas maduras."),
    Vino(bodegasMock[3], "Los Toneles Gran Reserva", 2014, "etiqueta_los_toneles_gran_reserva.jpg", 6400, maridajes[2], varietales[4], "Complejo con notas de chocolate, tabaco y vainilla.")
]
    
    for vino in vinosMock:
        vino.bodega.vinos.append(vino)

    # Usuarios
    usuario_1 = Usuario("ME_Jimenez", "contraseña1")
    usuario_2 = Usuario("David84", "constraseña2")
    usuario_3 = Usuario("Mica_Navarrete92", "constraseña3")
    usuario_4 = Usuario("Fran_89", "constraseña4")

    # Enófilos
    listaEnofilos = [
    Enofilo("María Elena", "Jimenez", None, usuario_1),
    Enofilo("David", "Iglesias", None, usuario_2),
    Enofilo("Micaela", "Navarrete", None, usuario_3),
    Enofilo("Francisco Miguel", "Morera", None, usuario_4)]

    for i in range(len(listaEnofilos)):
        listaEnofilos[i].siguiendo.append(Siguiendo(bodegasMock[i], datetime.datetime.now()))
    
    gestor.bodegas = bodegasMock
    gestor.maridajes = maridajes
    gestor.enofilos = listaEnofilos
    # Mostrar la pantalla y ejecutar el método del gestor
    pantalla.show()
    gestor.opcionImportarActualizacionVinos()

    # Ejecutar el loop de la aplicación
    sys.exit(app.exec_())