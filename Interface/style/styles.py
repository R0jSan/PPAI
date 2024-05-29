from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

FONT = "PMingLiU-ExtB"
TITLE_SIZE = 50
LABEL_SIZE = 15

def crearBox(title, text):
    error_box = QMessageBox()
    error_box.setWindowTitle(title)
    error_box.setText(text)
    error_box.setStyleSheet(stylesheet_error_box)
    error_box.exec_()

def crearLayout(widgetlist, layout):
    for widget in widgetlist:
        layout.addWidget(widget)

def alinear(text, size):
    text.setFont(QFont(FONT, size))
    text.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

stylesheet_error_box = '''
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

stylesheet_global = """
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