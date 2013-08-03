# -*- coding: cp1252 -*-

from PyQt4 import QtCore, QtGui
import sys
from ui_MainWindow import Ui_MainWindow
from Juego import Juego
import cPickle

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #Accion al momento de dar click en el boton Guardar
    def guardar(self):
        path = QtGui.QFileDialog.getSaveFileName(self,'Save File', '.sudo')
        if path != "":
            file_ = open(path,"wb")
            cPickle.dump(self.game,file_,protocol = 2)
            file_.close()

    def cargar(self):
        path = QtGui.QFileDialog.getOpenFileName(self,'Open File', '.sudo')
        if path != "":
            file_ = open(path,"rb")
            ob = cPickle.load(file_)
            self.game = ob


    def verificar(self):
        #Parsea los valores de la interfaz al tablero juego (correctamente)
        for i in range(0,9):
            for j in range(0,9):
                if self.ui.gridLayout.itemAtPosition(i,j).widget().isEnabled():
                    val = self.ui.gridLayout.itemAtPosition(i,j).widget().text()
                    val = val.toInt(base = 10)[0]
                    self.game.juego.getCell(i,j).setValue(val)

        #Pinta las celdas jugadas por defecto (blanco)
        for i in range(0,9):
            for j in range(0,9):
                val = self.ui.gridLayout.itemAtPosition(i,j).widget().isEnabled() #Si el qlineedit xy está habilitado se pinta de blanco
                if val:
                    pal = self.ui.gridLayout.itemAtPosition(i,j).widget().palette()
                    pal.setColor(QtGui.QPalette.Base, QtGui.QColor('White'))
                    self.ui.gridLayout.itemAtPosition(i,j).widget().setPalette(pal)


        #obtiene las celdas erróneas y las pinta de color (254,155,153)
        ls_error = []
        ls_error = self.game.tablero.compare(self.game.juego)

        print len(ls_error)

        for i in range(0,len(ls_error)):
            x = ls_error[i].getX()
            y = ls_error[i].getY()
            pal = self.ui.gridLayout.itemAtPosition(x,y).widget().palette()
            pal.setColor(QtGui.QPalette.Base, QtGui.QColor(254,155,153))
            self.ui.gridLayout.itemAtPosition(x,y).widget().setPalette(pal)


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
                    pal =  QtGui.QPalette(c.palette())
                    pal.setColor(QtGui.QPalette.Base,QtGui.QColor(0,204,51))
                    c.setPalette(pal)
                    c.setEnabled(False)
                    #c.setReadOnly(True)
                self.ui.gridLayout.addWidget(c,i,j)
        self.ui.txt_jugador.setText(name)
        self.ui.txt_nivel.setText(str(dif))


    #Intercambio de Datos de la Ventana Inicio a la ventana MainWindow
    def SetDatosPrincipales(self,jugador_nombre,value):
        self.ui.txt_jugador.setText(jugador_nombre);
        if value==1:
            self.ui.txt_nivel.setText("Fácil")
            print"facil"
            self.loadNew(jugador_nombre,1)
        elif value== 2:
            self.ui.txt_nivel.setText("Normal")
            print"Normal"
            self.loadNew(jugador_nombre,2)
        elif value== 3:
            self.ui.txt_nivel.setText("Avanzado")
            print"Avanzado"
            self.loadNew(jugador_nombre,3)
        else:
             self.ui.txt_nivel.setText("Experto")
             print"Experto"
             self.loadNew(jugador_nombre,4)


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    myapp.loadNew("pepe",1)
    #myapp.verificar()
    sys.exit(app.exec_())
    exit(app.exec_())
