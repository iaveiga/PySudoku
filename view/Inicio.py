# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicio.ui'
#
# Created: Sat Jul 20 18:46:52 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 350)
        Dialog.setWindowTitle(_fromUtf8("Inicio"))
        self.txt_nombre_jugador = QtGui.QLineEdit(Dialog)
        self.txt_nombre_jugador.setGeometry(QtCore.QRect(40, 90, 311, 20))
        self.txt_nombre_jugador.setObjectName(_fromUtf8("txt_nombre_jugador"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.rbt_facil = QtGui.QRadioButton(Dialog)
        self.rbt_facil.setGeometry(QtCore.QRect(50, 150, 82, 17))
        self.rbt_facil.setObjectName(_fromUtf8("rbt_facil"))
        self.rbt_normal = QtGui.QRadioButton(Dialog)
        self.rbt_normal.setGeometry(QtCore.QRect(120, 150, 82, 17))
        self.rbt_normal.setObjectName(_fromUtf8("rbt_normal"))
        self.rbt_avanzado = QtGui.QRadioButton(Dialog)
        self.rbt_avanzado.setGeometry(QtCore.QRect(200, 150, 82, 17))
        self.rbt_avanzado.setObjectName(_fromUtf8("rbt_avanzado"))
        self.rbt_experto = QtGui.QRadioButton(Dialog)
        self.rbt_experto.setGeometry(QtCore.QRect(290, 150, 82, 17))
        self.rbt_experto.setObjectName(_fromUtf8("rbt_experto"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_Jugar = QtGui.QPushButton(Dialog)
        self.btn_Jugar.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.btn_Jugar.setObjectName(_fromUtf8("btn_Jugar"))
        self.btn_cargar = QtGui.QPushButton(Dialog)
        self.btn_cargar.setGeometry(QtCore.QRect(150, 210, 91, 23))
        self.btn_cargar.setObjectName(_fromUtf8("btn_cargar"))
        self.btn_estadisticas = QtGui.QPushButton(Dialog)
        self.btn_estadisticas.setGeometry(QtCore.QRect(160, 240, 75, 23))
        self.btn_estadisticas.setObjectName(_fromUtf8("btn_estadisticas"))
        self.btn_salir = QtGui.QPushButton(Dialog)
        self.btn_salir.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_salir, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.Salir)
        QtCore.QObject.connect(self.btn_Jugar, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.Jugar)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.label.setText(_translate("Dialog", "Nombre", None))
        self.rbt_facil.setText(_translate("Dialog", "Facil", None))
        self.rbt_normal.setText(_translate("Dialog", "Normal", None))
        self.rbt_avanzado.setText(_translate("Dialog", "Avanzado", None))
        self.rbt_experto.setText(_translate("Dialog", "Experto", None))
        self.label_2.setText(_translate("Dialog", "Dificultad", None))
        self.btn_Jugar.setText(_translate("Dialog", "Jugar", None))
        self.btn_cargar.setText(_translate("Dialog", "Cargar Partida", None))
        self.btn_estadisticas.setText(_translate("Dialog", "Estadisticas", None))
        self.btn_salir.setText(_translate("Dialog", "Salir", None))
        self.label_3.setText(_translate("Dialog", "PY-SUDOKU", None))

