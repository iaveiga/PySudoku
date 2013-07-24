from PyQt4 import QtCore, QtGui
import sys
from Inicio import Ui_Dialog
from MainWindow import Ui_MainWindow 

class Inicio(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def Jugar(self):
        m = MainWindow()
        m.show()
        
    def Salir(self):
        sys.exit(0)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Inicio()
    myapp.show()
    sys.exit(app.exec_())
exit(app.exec_())
