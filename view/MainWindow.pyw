from PyQt4 import QtCore, QtGui
import sys
from MainWindow import Ui_MainWindow

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    '''
    def loadLE(self):
        for i in range(0,2):
            for j in range(0,1):
                lineE = QtGui.QLineEdit()
                self.ui.gridLayoutWidget.addWidget(lineE,i,j)
                lineE.show()
                
                self.ui.gridLayoutWidget.addWidget(self,lineE,i,j)
                lineE.setMaxLength(1)
                lineE.setInputMask("0")
                lineE.setFixedSize(30,30)
                lineE.show()
               
    '''
                
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
