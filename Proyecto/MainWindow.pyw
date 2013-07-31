from PyQt4 import QtCore, QtGui
import sys
from ui_MainWindow import Ui_MainWindow
from Juego import Juego
import cPickle

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.game = None

    #Accion al momento de dar click en el boton Guardar
    def Guardar(self):
        return 0     

    #Accion al momento de dar click en el boton Verificar
    def Verificar(self):
        return 0

    #Accion al momento de dar click en el submenu Salir
    def Salir(self):
        sys.exit(0)
                
    def loadNew(self, name = str, dif = int):
        #Falta pintar de color distinto
        self.game = Juego(name, dif)
        for i in range(9):
            for j in range(9):
                c = QtGui.QLineEdit()
                c.setMaxLength(1)
                c.setInputMask("0")
                c.setFixedSize(30,30)
                value = self.game.juego.getCell(i,j).getValue()
                if value != 0:
                    c.setText(str(value))
                    
                self.ui.gridLayout.addWidget(c,i,j)
                self.ui.txt_jugador.setText(str(name))
                self.ui.txt_nivel.setText(str(dif))
                
    def saveGame(path):
        file_ = open(path,"wb")
        cPickle.dump(self.game,file_,protocol = 2)
        file_.close()

    def loadGame(path):
        fie_ = open(path,"rb")
        ob = cPickle.load(file_)
        self.game = ob
        
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    myapp.loadNew("pepe",4)
    sys.exit(app.exec_())
    exit(app.exec_())
