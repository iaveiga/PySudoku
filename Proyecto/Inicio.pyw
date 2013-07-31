from PyQt4 import QtCore, QtGui
import sys
from ui_Inicio import Ui_Inicio_Frame

class Inicio(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Inicio_Frame()
        self.ui.setupUi(self)

    def Jugar(self):
        if(self.ui.txt_nombre_jugador.text()==""):
            print"positivo"
        
        
    def Salir(self):
        sys.exit(0)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Inicio()
    myapp.show()
    sys.exit(app.exec_())
exit(app.exec_())
