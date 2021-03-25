from random import *

from PyQt5 import QtCore, QtGui

from mydesign import Ui_MainWindow
import sys
import openpyxl
from PyQt5.QtWidgets import *


def start_excel():
    global sheets
    wb = openpyxl.load_workbook(filename="C:\Programming\Discover China\Discover China 1 all vocabulary.xlsx")
    sheets = [wb['unit 1'], wb['unit 2'], wb['unit 3'], wb['unit 4'], wb['unit 5'], wb['unit 6'],
              wb['unit 7'], wb['unit 8'], wb['unit 9'], wb['unit 10'], wb['unit 11'], wb['unit 12']]


def get_random_cell(unit):
    cell_num = str(randint(1, 50))
    cell = sheets[unit]['A' + cell_num]
    while cell.value == '' or cell.value is None:
        cell_num = str(randint(1, 50))
        cell = sheets[unit]['A' + cell_num]
    return cell_num


class mywindow(QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cell_num = 0
        self.right_ans = None
        self.unit = 1
        self.ui.nextq.setStyleSheet('background: #86f353; border: 1px solid #86f353;padding: 6px;')
        self.ui.centralwidget.setStyleSheet('background: white')
        self.ui.question.adjustSize()
        self.ui.result.adjustSize()

        self.ui.choose_mode.addItem("Choose pinyin")

        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.exit_btn = QToolButton()
        self.exit_btn.setText("Main menu")
        self.exit_btn.clicked.connect(self.beginning)
        self.toolbar.addAction(exitAction)
        self.toolbar.addWidget(self.exit_btn)
        self.addToolBar(self.toolbar)

        self.ui.option_1.clicked.connect(self.choosed_option_1)
        self.ui.option_2.clicked.connect(self.choosed_option_2)
        self.ui.option_3.clicked.connect(self.choosed_option_3)
        self.ui.option_4.clicked.connect(self.choosed_option_4)
        self.ui.nextq.clicked.connect(self.new_question)
        self.ui.play_btn.clicked.connect(self.start_game)

        self.beginning()
        self.setWindowTitle("DC")
        self.resize(362, 450)
        self.resized.connect(self.resizing)

    def beginning(self):
        self.hide_question()
        self.ui.formLayoutWidget_2.show()  # main_menu_layout

    def start_game(self):
        self.unit = int(self.ui.choose_unit.value()) - 1
        self.ui.formLayoutWidget_2.hide()   #main_menu_layout
        self.ui.verticalLayoutWidget.show() #choose_layout
        self.new_question()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(mywindow, self).resizeEvent(event)

    def resizing(self):
        self.ui.choose_layout.setGeometry(QtCore.QRect(0, 20, self.width(), 261))
        self.ui.nextq.setFixedWidth(self.width())
        self.ui.main_menu_layout.setGeometry(QtCore.QRect(0, 20, self.width(), 261))


    def hide_question(self):
        self.ui.verticalLayoutWidget.hide()
        self.ui.nextq.hide()

    def make_all_btns_white_and_clear_labels(self):
        self.ui.verticalLayoutWidget.show() #choose_layout
        self.ui.option_1.setStyleSheet('background: #c8c8c8; border: 1px solid #c8c8c8;padding: 6px;')
        self.ui.option_2.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 6px;')
        self.ui.option_3.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 6px;')
        self.ui.option_4.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 6px;')
        self.ui.nextq.hide()
        self.ui.result.setText("")

    def new_question(self):
        self.make_all_btns_white_and_clear_labels()
        self.cell_num = get_random_cell(self.unit)
        self.ui.question.setText(sheets[self.unit]['A' + self.cell_num].value.strip())
        options = [self.ui.option_1, self.ui.option_2, self.ui.option_3, self.ui.option_4]
        answers = [self.cell_num]
        self.right_ans = randint(0, 3)
        options[self.right_ans].setText(sheets[self.unit]['B' + self.cell_num].value)
        options.pop(self.right_ans)
        for o in options:
            rand_cell_num = get_random_cell(self.unit)
            while rand_cell_num in answers:
                rand_cell_num = get_random_cell(self.unit)
            o.setText(sheets[self.unit]['B' + rand_cell_num].value)
            answers.append(rand_cell_num)

    def choosed_option_1(self):
        if self.right_ans == 0:
            self.ui.option_1.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.ui.result.setText(sheets[self.unit]['C' + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_1.setStyleSheet('background: red;border: 1px solid red;padding: 6px;')

    def choosed_option_2(self):
        if self.right_ans == 1:
            self.ui.option_2.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.ui.result.setText(sheets[self.unit]['C' + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_2.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 6px;')

    def choosed_option_3(self):
        if self.right_ans == 2:
            self.ui.option_3.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.ui.result.setText(sheets[self.unit]['C' + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_3.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 6px;')

    def choosed_option_4(self):
        if self.right_ans == 3:
            self.ui.option_4.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.ui.result.setText(sheets[self.unit]['C' + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_4.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 6px;')


if __name__ == '__main__':
    start_excel()
    app = QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
