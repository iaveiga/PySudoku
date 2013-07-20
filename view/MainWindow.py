# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sun Jul 14 19:34:40 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(848, 600)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 631, 431))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(320, 470, 151, 51))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 480, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_guardar = QtGui.QPushButton(self.centralwidget)
        self.btn_guardar.setGeometry(QtCore.QRect(720, 220, 75, 23))
        self.btn_guardar.setObjectName(_fromUtf8("btn_guardar"))
        self.lbl_jugador = QtGui.QLabel(self.centralwidget)
        self.lbl_jugador.setGeometry(QtCore.QRect(680, 110, 46, 13))
        self.lbl_jugador.setObjectName(_fromUtf8("lbl_jugador"))
        self.txt_jugador = QtGui.QLineEdit(self.centralwidget)
        self.txt_jugador.setEnabled(False)
        self.txt_jugador.setGeometry(QtCore.QRect(682, 130, 151, 20))
        self.txt_jugador.setObjectName(_fromUtf8("txt_jugador"))
        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(680, 160, 91, 16))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.txt_nivel = QtGui.QLineEdit(self.centralwidget)
        self.txt_nivel.setEnabled(False)
        self.txt_nivel.setGeometry(QtCore.QRect(682, 180, 151, 20))
        self.txt_nivel.setObjectName(_fromUtf8("txt_nivel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuardar = QtGui.QAction(MainWindow)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionSALIR = QtGui.QAction(MainWindow)
        self.actionSALIR.setObjectName(_fromUtf8("actionSALIR"))
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSALIR)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PY - SUDOKU", None))
        self.label.setText(_translate("MainWindow", "TIEMPO:", None))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar", None))
        self.lbl_jugador.setText(_translate("MainWindow", "Jugador:", None))
        self.label2.setText(_translate("MainWindow", "Nivel de Juego: ", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar", None))
        self.actionSALIR.setText(_translate("MainWindow", "Salir", None))

