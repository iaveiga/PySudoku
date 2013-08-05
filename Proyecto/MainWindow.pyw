# -*- coding: cp1252 -*-

from PyQt4 import QtCore, QtGui
import sys
from ui_MainWindow import Ui_MainWindow
from Juego import Juego
import cPickle
import random

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        """
            Constructor de la clase MainWindow.
        """
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.crear() #crea los qlineedit vacíos

    def guardar(self):
        """
            Guarda una partida de Sudoku con lo siguiente:
            * Nombre del Jugador.
            * Dificultad.
            * Tablero completo.
            * Tablero a jugar progresado.
            * Tiempo de juego.
            El objeto se serializa y se almacena en un archivo .sudo .
            @author Iván Aveiga
        """
        self.StopTimer()
        self.game.time = self.getTime()
        print(self.game.time)
        path = QtGui.QFileDialog.getSaveFileName(self,'Save File', '.sudo')
        if path != "":
            self.parse()
            file_ = open(path,"wb")
            cPickle.dump(self.game,file_,protocol = 2)
            file_.close()
        self.timer.start()

    def cargar(self):
        """
            Carga una partida de Sudoku almacenada en un archivo .sudo .
            @author Iván Aveiga.
        """
        path = QtGui.QFileDialog.getOpenFileName(self,'Open File', '.sudo')
        if path != "":
            file_ = open(path,"rb")
            ob = cPickle.load(file_)
            self.game = ob

    def parse(self):
        """
            Pasa los valores de la interfaz gráfica al tablero de Sudoku interno.
            @author Iván Aveiga.
        """
        for i in range(0,9):
            for j in range(0,9):
                if self.ui.gridLayout.itemAtPosition(i,j).widget().isEnabled():
                    val = self.ui.gridLayout.itemAtPosition(i,j).widget().text()
                    val = val.toInt(base = 10)[0]
                    self.game.juego.getCell(i,j).setValue(val)

    #CRONOMETRO
        #inicializando el cronometro
    def InitTimer(self,seg):
        """
            Se inicia el contador del tiempo en segundos = 0
            y se hace la conexion con la funcion count
            @author Kevin Campuzano
        """
        self.ss = seg
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.count)
        self.timer.start(1000)
        self.time_n= str(self.ss/60)+ ":" + str(self.ss%60)
        self.ui.lcdNumber.display(self.time_n)

    def count(self):
        """
            Se empieza el contador del tiempo, cada en cuanto se va
            agregando un segundo, los minutos se los maneja con los segundos
            @author Kevin Campuzano
        """
        self.ss = self.ss + 1
        self.time_n= str(self.ss/60)+ ":" + str(self.ss%60)
        self.ui.lcdNumber.display(self.time_n)
        self.ui.lcdNumber.show()

    def StopTimer(self):
        """
            Funcion con la que se detiene el count del tiempo
            @author Kevin Campuzano
        """
        self.timer.stop()

    def getTime(self):
        """
            GetTime, obtiene los segundos del juego
            @author Kevin Campuzano
        """
        return(self.ss)
        print(self.ss)

    def verificar(self):
        """
            Verifica que esté correctamente resuelto el Sudoku.
            Para esto
            -Se obtiene los valores de la interfaz gráfica
            -Se obtiene las celdas habilitadas (celdas a completar).
            -Se pinta todas estas celdas de color blanco
            -Se cuenta cuántas celdas están con valores en blanco.
            -Se compara los sudokus (sudoku completo, sudoku jugado).
            -Se obtiene la lista de celdas erróneas y se pintan de otro color.
            -Si no hay celdas en blanco y si no hay celdas erróneas el jugador ganó el juego.
            -Si no usó ayudas y dependiendo del tiempo ingresa al ranking.
            @author Iván Aveiga.
        """
        self.parse()
        cont = 0
        for i in range(0,9):
            for j in range(0,9):
                habilitado = self.ui.gridLayout.itemAtPosition(i,j).widget().isEnabled() #Si el qlineedit xy está habilitado se pinta de blanco
                val = self.ui.gridLayout.itemAtPosition(i,j).widget().text()
                val = val.toInt(base = 10)[0]
                if habilitado:
                    color = QtGui.QColor("White")
                    self.pintar(i,j,color)
                    if val not in [1,2,3,4,5,6,7,8,9]:
                        cont += 1

        ls_error = self.game.tablero.compare(self.game.juego)
        for i in range(0,len(ls_error)):
            x = ls_error[i].getX()
            y = ls_error[i].getY()
            color = QtGui.QColor(254,155,153)
            self.pintar(x,y,color)

        if len(ls_error) == 0 and cont == 0:
            self.timer.stop()
            for i in range(0,9):
                for j in range(0,9):
                    self.ui.gridLayout.itemAtPosition(i,j).widget().setEnabled(False)
            nombre = self.game.nombre
            ayuda = str(5 - self.game.hints)
            msg = "Felicitaciones " + nombre + " \nGanaste usando " + ayuda + " ayudas."
            resp = QtGui.QMessageBox.information(self, "PySudoku", msg, QtGui.QMessageBox.Ok)
            if self.game.hints == 5:
                time = self.getTime()
                resp_ = self.setRanking(str(nombre), time)
                if resp_:
                    msg = "Felicitaciones " + nombre + " \nAcabas de entrar al ranking.!!"
                    resp = QtGui.QMessageBox.information(self, "PySudoku", msg, QtGui.QMessageBox.Ok)




    def pintar(self,x = int, y = int, color = QtGui.QColor):
        """
            Cambia el color de fondo de un qlineedit.
            @param x, coordenada en x del qlineedit.
            @param y, coordenada en y del qlineedit.
            @param color, color a setear.
            @author Iván Aveiga.
        """
        pal = self.ui.gridLayout.itemAtPosition(x,y).widget().palette()
        pal.setColor(QtGui.QPalette.Base,QtGui.QColor(color))
        self.ui.gridLayout.itemAtPosition(x,y).widget().setPalette(pal)

    def setRanking(self, name = str, time = int):
        flag = False
        file_ = open("stats.txt","r")
        lines = file_.readlines()
        line = name + "," + str(time) + "\n"
        file_.close()

        for i in range(0,len(lines)):
            l = lines[i].rstrip("\n").split(",")
            if time < int(l[1]):
                lines[i] = line
                flag = True
                break
        for i in range(0,len(lines)):
            print lines[i]

        f = open("stats.txt","w")
        f.writelines(lines)
        f.close()

        return flag


    def Salir(self):
        """
            Sale de la aplicación.
            @author Kevin Campuzano.
        """
        sys.exit(0)

    def crear(self):
        """
            Añade 9x9 qlineedit en un Gridlayout a jugar con la configuración de longitud,
            valores soportados, tamaño.
            @author Iván Aveiga
        """
        for i in range(0,9):
            for j in range(0,9):
                c = QtGui.QLineEdit()
                c.setMaxLength(1)
                c.setInputMask("0")
                c.setFixedSize(30,30)
                self.ui.gridLayout.addWidget(c,i,j)

    def loadNew(self, name = str, dif = int, saved = bool):
        """
            Carga los valores del juego a la interfaz gráfica.
            @param name, nombre del jugador.
            @param dif, dificultad del juego.
            @param saved, si es un juego guardado o no.
            @author Iván Aveiga.
            @author Kevin Campuzano.
        """

        """
            Si no es un juego guardado crea un nuevo juego
        """
        if not saved:
            self.game = Juego(name, dif)
            self.game.nombre = name
            self.game.dif = dif
            self.InitTimer(0)
        else:
            self.cargar()
            self.InitTimer(self.game.time)

        """
            Pasa los valores a la interfaz, las celdas a no jugar(celdas por defecto) son
            deshabilitadas y son pintadas de color verde. Además que indica el nombre y
            la dificultad del jugador en la pantalla.
        """
        for i in range(9):
            for j in range(9):
                value = self.game.juego.getCell(i,j).getValue()
                flag = 0
                color = QtGui.QColor("White")
                if value != 0: #Si es una celda no ocupada
                    self.ui.gridLayout.itemAtPosition(i,j).widget().setText(str(value)) #pasa el valor a la interfaz
                    if self.game.juego.getCell(i,j).getOccupied():
                        flag = 1
                        self.ui.gridLayout.itemAtPosition(i,j).widget().setEnabled(False)
                if flag == 1:
                    color = QtGui.QColor(0,204,51)
                self.pintar(i,j,color)
        self.ui.txt_jugador.setText(self.game.nombre)
        if self.game.dif == 1:
            self.ui.txt_nivel.setText("Fácil")
        elif self.game.dif == 2:
            self.ui.txt_nivel.setText("Normal")
        elif self.game.dif == 3:
            self.ui.txt_nivel.setText("Avanzado")
        else:
            self.ui.txt_nivel.setText("Experto")

    #Intercambio de Datos de la Ventana Inicio a la ventana MainWindow
    def SetDatosPrincipales(self,jugador_nombre,value):
        """
            Recibe los datos de la ventana de inicio y crea un nuevo juego.
            @param jugador_nombre, nombre del jugador.
            @param value, dificultad del juego
            @author Kevin Campuzano
        """
        self.ui.txt_jugador.setText(jugador_nombre);
        if value==1:
            self.ui.txt_nivel.setText("Fácil")
            self.loadNew(jugador_nombre,1, False)
        elif value== 2:
            self.ui.txt_nivel.setText("Normal")
            self.loadNew(jugador_nombre,2, False)
        elif value== 3:
            self.ui.txt_nivel.setText("Avanzado")
            self.loadNew(jugador_nombre,3, False)
        else:
             self.ui.txt_nivel.setText("Experto")
             self.loadNew(jugador_nombre,4, False)

    def ayuda(self):
        """
            Implementa las ayudas del juego.
            Si tiene ayudas disponibles, coloca el valor correcto de una de las celdas a jugar e
            inhabilita la celda y se cambia el color de fondo para indicar que ha sido generado
            por el juego..
            Si no tiene ayudas disponibles se inhabilita el botón de ayudas.
            @author Iván Aveiga, Kevin Campuzano.
        """
        if self.game.hints > 0:
            x = random.randint(0,8)
            y = random.randint(0,8)
            while not self.ui.gridLayout.itemAtPosition(x,y).widget().isEnabled():
                x = random.randint(0,8)
                y = random.randint(0,8)
            val = self.game.tablero.getCell(x,y).getValue()
            self.game.juego.getCell(x,y).setValue(val)
            self.ui.gridLayout.itemAtPosition(x,y).widget().setText(str(val))
            self.ui.gridLayout.itemAtPosition(x,y).widget().setEnabled(False)
            color = QtGui.QColor(0,255,204)
            self.pintar(x,y,color)
            self.game.hints -= 1
        if self.game.hints == 0:
            self.ui.btn_Ayuda.setEnabled(False)
