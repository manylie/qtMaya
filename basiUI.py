from maya import cmds 
from PySide2 import QtWidgets, QtGui
from PySide2.QtUiTools import QUiLoader
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

class TRSConnectorWindow(MayaQWidgetBaseMixin, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(TRSConnectorWindow, self).__init__(*args, **kwargs)

        # Cargar archivo .ui
        self.widget = QUiLoader().load(r"D:/qtMaya/basiUI.ui")  # Editar ruta
        self.setWindowTitle(self.widget.windowTitle())
        self.setCentralWidget(self.widget)
        
        # Conectar el botón
        self.widget.pushButton_3.clicked.connect(self.btn3)
        self.widget.pushButton.clicked.connect(self.btn)
        self.widget.pushButton_2.clicked.connect(self.btn2)
        self.widget.checkBox.toggled.connect(self.check)

    def check(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("check presionado")
        msg.exec_()  # Mostrar el cuadro de mensaje
    def btn3(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("pushButton_3 boton")
        msg.exec_()  # Mostrar el cuadro de mensaje
    def btn(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("pushButton_3 boton")
        msg.exec_()  # Mostrar el cuadro de mensaje
    def btn2(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("pushButton_3 boton")
        msg.exec_()  # Mostrar el cuadro de mensaje

# Verificar y mostrar la ventana
def show_TRSConnectorWindow():
    if cmds.window("TRSConnectorWindow", exists=True):
        cmds.deleteUI("TRSConnectorWindow", window=True)
    global mu
    mu = TRSConnectorWindow()
    mu.setObjectName("TRSConnectorWindow")
    mu.show()

# Llamada para mostrar la ventana
show_TRSConnectorWindow()
