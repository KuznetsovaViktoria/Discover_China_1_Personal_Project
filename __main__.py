from PyQt5.QtGui import QIcon

from mydesign import Ui_MainWindow
import sys
import openpyxl
from PyQt5.QtWidgets import *

def start_excel():
    global wb, sheet, vals
    wb = openpyxl.load_workbook(filename="C:\Programming\Discover China\Discover China 1 all vocabulary.xlsx")
    sheet = wb['unit 1']
    vals = [v[0].value for v in sheet['A1:A2']]

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.setMovable(False)

        self.ui.nextq.hide()

        self.setWindowTitle("DC")
        self.resize(600, 400)


if __name__ == '__main__':
    start_excel()
    app = QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())



