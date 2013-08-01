from PyQt4 import QtCore, QtGui
import sys
from ui_Inicio import Ui_Inicio_Frame
from MainWindow import MainWindow


class Inicio(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Inicio_Frame()
        self.ui.setupUi(self)

    def Jugar(self):
        if(self.ui.rbt_facil.isChecked() and self.ui.txt_nombre_jugador.text != ""):
            #mando a ventana MainWindow (nombre,1)
            print"n,1"
            self.setVisible(False)
            self.w = MainWindow()
            self.w.show()
        elif(self.ui.rbt_normal.isChecked() and self.ui.txt_nombre_jugador.text != ""):
            #mando a ventana MainWindow (nombre,2)
            print"n,2"
            self.setVisible(False)
            self.w = MainWindow()
            self.w.show()
        elif(self.ui.rbt_avanzado.isChecked() and self.ui.txt_nombre_jugador.text != ""):
            #mando a ventana MainWindow (nombre,3)
            print"n,3"
            self.setVisible(False)
            self.w = MainWindow()
            self.w.show()
        elif(self.ui.rbt_experto.isChecked() and self.ui.txt_nombre_jugador.text != ""):
            #mando a ventana MainWindow (nombre,4)
            print"n,4"
            self.setVisible(False)
            self.w = MainWindow()
            self.w.show()
        else:
            #No ha dado en ni un radioButton o no ha puesto el nombre o no ha hecho ninguno de los dos 
            print"Faltan campos a completar"

    def Salir(self):
        sys.exit(0)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Inicio()
    myapp.show()
    sys.exit(app.exec_())
exit(app.exec_())
