# -*- coding: cp1252 -*-
from PyQt4 import QtCore, QtGui
import sys
from ui_Inicio import Ui_Inicio_Frame
from MainWindow import MainWindow


class Inicio(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Inicio_Frame()
        self.ui.setupUi(self)

    def Stats(self):
        """
            Muestra las estadísticas en un informationBox.
            No se muestra el nivel en que se resolvió el Sudoku.
            Se muestra en el formato minutos:segundos.
            @author Iván Aveiga.
        """
        file_= open("stats.txt","r")
        lines = file_.readlines()
        msg = ""
        for i in range(0,len(lines)):
            aux = lines[i].rstrip("\n").split(",")
            t = int(aux[1])
            time = "(" + str(t/60) + " : " + str(t %60) + ")"
            msg = msg + aux[0] + "\n" + time + "\n \n"
        file_.close()
        rs = QtGui.QMessageBox.information(self, "Rankings",  msg, QtGui.QMessageBox.Ok)

    def Jugar(self):
        """
            Manda la comunicacion del nombre junto con el nivel de dificultad escogido por el usuario
            a la ventana de Juego, se valida que en el caso de que el campo de nombre este vacio no le permita continuar
            al juego, tambien se valida que si ninguna dificultad esta selecciona no le permita jugar
            @author Kevin Campuzano.
        """
        if(self.ui.rbt_facil.isChecked() and self.ui.txt_nombre_jugador.text() != ""):
            #mando a ventana MainWindow(nombre del Jugador ,Dificultad:1)
            self.setVisible(False)
            self.w = MainWindow()
            self.w.SetDatosPrincipales(self.ui.txt_nombre_jugador.text(),1)
            self.w.show()

        elif(self.ui.rbt_normal.isChecked() and self.ui.txt_nombre_jugador.text() != ""):
            #mando a ventana MainWindow(Nombre del Jugador, Dificultad:2)
            self.setVisible(False)
            self.w = MainWindow()
            self.w.SetDatosPrincipales(self.ui.txt_nombre_jugador.text(),2)
            self.w.show()

        elif(self.ui.rbt_avanzado.isChecked() and self.ui.txt_nombre_jugador.text() != ""):
            #mando a ventana MainWindow(Nombre del Jugador,Dificultad:3)
            self.setVisible(False)
            self.w = MainWindow()
            self.w = MainWindow()
            self.w.SetDatosPrincipales(self.ui.txt_nombre_jugador.text(),3)
            self.w.show()

        elif(self.ui.rbt_experto.isChecked() and self.ui.txt_nombre_jugador.text() != ""):
            #mando a ventana MainWindow(Nombre del Jugador,Dificultad:4)
            self.setVisible(False)
            self.w = MainWindow()
            self.w.SetDatosPrincipales(self.ui.txt_nombre_jugador.text(),4)
            self.w.show()

        else:
            resp = QtGui.QMessageBox.critical(self, "PySudoku", "Ingrese nombre y/o seleccione dificultad", QtGui.QMessageBox.Ok)
            #No ha dado en ni un radioButton o no ha puesto el nombre o no ha hecho ninguno de los dos

    def Cargar(self):
         """
            Evento que realiza el boton cargar, que es el cual carga el juego antiguo y lo setea para volver a jugar.
            @author Kevin Campuzano.
        """
        self.w = MainWindow()
        self.w.loadNew(" ", 0, True)
        self.setVisible(False)
        self.w.show()

    def Salir(self):
         """
            Evento para salir del juego
            @author Kevin Campuzano.
        """
        sys.exit(0)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Inicio()
    myapp.show()
    sys.exit(app.exec_())
exit(app.exec_())
