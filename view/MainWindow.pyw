from PyQt4 import QtCore, QtGui
import sys
from MainWindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        for i in range(9):
            for j in range(9):
                c = QtGui.QLineEdit()
                c.setMaxLength(1)
                c.setInputMask("0")
                c.setFixedSize(30,30)
                self.ui.gridLayout.addWidget(c,i,j)
        
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
exit(app.exec_())
