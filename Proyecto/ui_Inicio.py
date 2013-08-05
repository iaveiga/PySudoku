# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicio.ui'
#
# Created: Wed Jul 31 11:37:34 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Inicio_Frame(object):
    def setupUi(self, Inicio_Frame):
        Inicio_Frame.setObjectName(_fromUtf8("Inicio_Frame"))
        Inicio_Frame.resize(400, 350)
        Inicio_Frame.setWindowTitle(_fromUtf8("Inicio"))
        self.txt_nombre_jugador = QtGui.QLineEdit(Inicio_Frame)
        self.txt_nombre_jugador.setGeometry(QtCore.QRect(40, 90, 311, 20))
        self.txt_nombre_jugador.setObjectName(_fromUtf8("txt_nombre_jugador"))
        self.label = QtGui.QLabel(Inicio_Frame)
        self.label.setGeometry(QtCore.QRect(40, 70, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.rbt_facil = QtGui.QRadioButton(Inicio_Frame)
        self.rbt_facil.setGeometry(QtCore.QRect(50, 150, 82, 17))
        self.rbt_facil.setObjectName(_fromUtf8("rbt_facil"))
        self.rbt_normal = QtGui.QRadioButton(Inicio_Frame)
        self.rbt_normal.setGeometry(QtCore.QRect(120, 150, 82, 17))
        self.rbt_normal.setObjectName(_fromUtf8("rbt_normal"))
        self.rbt_avanzado = QtGui.QRadioButton(Inicio_Frame)
        self.rbt_avanzado.setGeometry(QtCore.QRect(200, 150, 82, 17))
        self.rbt_avanzado.setObjectName(_fromUtf8("rbt_avanzado"))
        self.rbt_experto = QtGui.QRadioButton(Inicio_Frame)
        self.rbt_experto.setGeometry(QtCore.QRect(290, 150, 82, 17))
        self.rbt_experto.setObjectName(_fromUtf8("rbt_experto"))
        self.label_2 = QtGui.QLabel(Inicio_Frame)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_Jugar = QtGui.QPushButton(Inicio_Frame)
        self.btn_Jugar.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.btn_Jugar.setObjectName(_fromUtf8("btn_Jugar"))
        self.btn_cargar = QtGui.QPushButton(Inicio_Frame)
        self.btn_cargar.setGeometry(QtCore.QRect(150, 210, 91, 23))
        self.btn_cargar.setObjectName(_fromUtf8("btn_cargar"))
        self.btn_estadisticas = QtGui.QPushButton(Inicio_Frame)
        self.btn_estadisticas.setGeometry(QtCore.QRect(160, 240, 75, 23))
        self.btn_estadisticas.setObjectName(_fromUtf8("btn_estadisticas"))
        self.btn_salir = QtGui.QPushButton(Inicio_Frame)
        self.btn_salir.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.label_3 = QtGui.QLabel(Inicio_Frame)
        self.label_3.setGeometry(QtCore.QRect(140, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Inicio_Frame)
        QtCore.QObject.connect(self.btn_salir, QtCore.SIGNAL(_fromUtf8("clicked()")), Inicio_Frame.Salir)
        QtCore.QObject.connect(self.btn_Jugar, QtCore.SIGNAL(_fromUtf8("clicked()")), Inicio_Frame.Jugar)
        QtCore.QObject.connect(self.btn_cargar, QtCore.SIGNAL(_fromUtf8("clicked()")), Inicio_Frame.Cargar)
        QtCore.QObject.connect(self.btn_estadisticas, QtCore.SIGNAL(_fromUtf8("clicked()")), Inicio_Frame.Stats)
        QtCore.QMetaObject.connectSlotsByName(Inicio_Frame)

    def retranslateUi(self, Inicio_Frame):
        self.label.setText(_translate("Inicio_Frame", "Nombre", None))
        self.rbt_facil.setText(_translate("Inicio_Frame", "Fácil", None))
        self.rbt_normal.setText(_translate("Inicio_Frame", "Normal", None))
        self.rbt_avanzado.setText(_translate("Inicio_Frame", "Avanzado", None))
        self.rbt_experto.setText(_translate("Inicio_Frame", "Experto", None))
        self.label_2.setText(_translate("Inicio_Frame", "Dificultad", None))
        self.btn_Jugar.setText(_translate("Inicio_Frame", "Jugar", None))
        self.btn_cargar.setText(_translate("Inicio_Frame", "Cargar Partida", None))
        self.btn_estadisticas.setText(_translate("Inicio_Frame", "Estadísticas", None))
        self.btn_salir.setText(_translate("Inicio_Frame", "Salir", None))
        self.label_3.setText(_translate("Inicio_Frame", "PY-SUDOKU", None))

