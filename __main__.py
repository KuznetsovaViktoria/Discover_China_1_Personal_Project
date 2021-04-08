from random import *

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont

from mydesign import Ui_MainWindow
import sys
import openpyxl
from PyQt5.QtWidgets import *
from functools import partial
from time import *
from threading import Timer


def start_excel():
    global sheets
    wb = openpyxl.load_workbook(filename="C:\Programming\Discover China\Discover China 1 all vocabulary.xlsx")
    sheets = [wb['unit 1'], wb['unit 2'], wb['unit 3'], wb['unit 4'], wb['unit 5'], wb['unit 6'],
              wb['unit 7'], wb['unit 8'], wb['unit 9'], wb['unit 10'], wb['unit 11'], wb['unit 12']]


def get_random_cell(unit, q_col):
    cell_num = str(randint(1, 50))
    cell = sheets[unit][q_col + cell_num]
    while cell.value == '' or cell.value is None:
        cell_num = str(randint(1, 50))
        cell = sheets[unit][q_col + cell_num]
    return cell_num


class mywindow(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.question_list = [self.ui.question, self.ui.ex_info, self.ui.option_1, self.ui.option_2, self.ui.option_3,
                              self.ui.option_4]
        self.pairs_btn_list = [self.ui.btn1, self.ui.btn2, self.ui.btn3, self.ui.btn4, self.ui.btn5, self.ui.btn6,
                               self.ui.btn7, self.ui.btn8, self.ui.btn9, self.ui.btn10, self.ui.btn11, self.ui.btn12]
        self.made_pairs = []   # what pairs has been made in pair mode
        self.pair_mode_clicked_btns = []    # what buttons has been clicked in pair mode
        self.list_of_hierogliphs = []   # which buttons in pair mode is hierogliphs
        self.cell_num = 0  # cell number with the right answer
        self.right_ans = None  # the answer
        self.unit = 1  # choosed unit
        self.mode = "Choose pinyin"
        self.q_col = 'A'  # column in the excel table, from where we take questions, depends on the choosed mode
        self.a_col = 'B'  # column in the excel table, from where we take answers, depends on the choosed mode
        self.ex_col = 'C'  # the third column to show full information about the word after the right answer
        self.ui.nextq.setStyleSheet('background: #86f353; border: 1px solid #86f353;padding: 6px;')
        self.ui.centralwidget.setStyleSheet('background: white')

        self.ui.question.adjustSize()
        self.ui.ex_info.adjustSize()

        self.ui.choose_mode.addItem("Choose pinyin")
        self.ui.choose_mode.addItem("Choose hieroglyph")
        self.ui.choose_mode.addItem("Choose translation")
        self.ui.choose_mode.addItem("Choose pairs")

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
        self.ui.nextq.clicked.connect(self.next_question)
        self.ui.play_btn.clicked.connect(self.start_playing)
        self.ui.choose_mode.activated[str].connect(self.onActivated_choosing_mode)
        for i in range(12):
            self.pairs_btn_list[i].clicked.connect(partial(self.btn_pair_mode_been_clicked, i))

        self.beginning()
        self.setWindowTitle("DC")
        self.resize(550, 600)
        self.resized.connect(self.resizing)

    def beginning(self):
        self.hide_question()
        self.ui.formLayoutWidget_2.show()  # main_menu_layout

    def start_playing(self):
        self.unit = int(self.ui.choose_unit.value()) - 1
        self.ui.formLayoutWidget_2.hide()  # main_menu_layout
        if self.mode == "Choose pairs":
            self.ui.gridLayoutWidget.show() # pairs_layout
            self.new_pair_question()
        else:
            self.ui.verticalLayoutWidget.show()  # choose_layout
            self.new_question()

    def next_question(self):
        if self.mode == "Choose pairs":
            self.new_pair_question()
        else:
            self.new_question()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(mywindow, self).resizeEvent(event)

    def resizing(self):
        self.ui.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()))  # main_menu_layout
        self.ui.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, self.width(), int(self.height()*0.66))) # choose_layout
        self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, self.width(), int(self.height()*0.63)))   # pairs layout
        for w in self.question_list:
            w.setMinimumSize(QtCore.QSize(0, int(self.height()*0.1))) # разобраться, почему последний виджет меньше по высоте
        self.ui.nextq.setGeometry(QtCore.QRect(1, int(self.height()*0.7), self.width(), int(self.height()*0.11)))


    def onActivated_choosing_mode(self, mode):
        if mode == "Choose pinyin":
            self.mode = "Choose pinyin"
            self.q_col = 'A'
            self.a_col = 'B'
            self.ex_col = 'C'
        elif mode == "Choose hieroglyph":
            self.mode = "Choose hieroglyph"
            self.q_col = 'C'
            self.a_col = 'A'
            self.ex_col = 'B'
        elif mode == "Choose translation":
            self.mode = "Choose translation"
            self.q_col = 'A'
            self.a_col = 'C'
            self.ex_col = 'B'
        elif mode == "Choose pairs":
            self.mode = "Choose pairs"

    def hide_question(self):
        self.ui.verticalLayoutWidget.hide()
        self.ui.gridLayoutWidget.hide()
        self.ui.nextq.hide()

    def new_pair_question(self):
        self.made_pairs = []
        self.pair_mode_clicked_btns = []
        self.make_all_btns_white_and_clear_labels()
        b = [i for i in range(1, 50)]
        shuffle(b)
        a = []
        i = 0
        while len(a) < 6:
            if sheets[self.unit]['A' + str(b[i])].value != None:
                a.append(b[i])
            i+=1
        b = [i for i in range(12)]
        shuffle(b)
        b = [[b[0], b[1]], [b[2], b[3]], [b[4], b[5]], [b[6], b[7]], [b[8], b[9]], [b[10], b[11]]]
        self.right_ans = b
        o = 0
        for i in self.right_ans:
            self.pairs_btn_list[i[0]].setText(sheets[self.unit]['A' + str(a[o])].value)
            self.pairs_btn_list[i[1]].setText(sheets[self.unit]['C' + str(a[o])].value)
            o+=1
            self.pairs_btn_list[i[0]].setFont(QFont('SimSun', 24))
            self.pairs_btn_list[i[1]].setFont(QFont('SimSun', 20 - int(0.55*len(self.pairs_btn_list[i[1]].text()))))

    def check_pair(self):
        a = self.pair_mode_clicked_btns[0]
        b = self.pair_mode_clicked_btns[1]
        if [a, b] in self.right_ans or [b, a] in self.right_ans:
            self.made_pairs.append(a)
            self.made_pairs.append(b)
            self.pairs_btn_list[a].setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.pairs_btn_list[b].setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.pairs_btn_list[a].setEnabled(False)
            self.pairs_btn_list[b].setEnabled(False)
        else:
            self.pairs_btn_list[a].setStyleSheet('background: red;border: 1px solid red;padding: 6px;')
            self.pairs_btn_list[b].setStyleSheet('background: red;border: 1px solid red;padding: 6px;')
            t = Timer(1, self.pair_mode_change_btn_color_to_white, args=[a, b], kwargs=None)
            t.start()
        if len(self.made_pairs) == 12:
            self.ui.nextq.show()

    def pair_mode_change_btn_color_to_white(self, *n):
        for i in n:
            self.pairs_btn_list[i].setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 6px;')

    def btn_pair_mode_been_clicked(self, n):
        if self.pair_mode_clicked_btns == []:
            self.pair_mode_clicked_btns.append(n)
            self.pairs_btn_list[n].setStyleSheet('background: #c8c8c8;border: 2px solid black;padding: 6px;')
        elif self.pair_mode_clicked_btns == [n]:
            self.pair_mode_clicked_btns = []
            self.pairs_btn_list[n].setStyleSheet('background: #c8c8c8;border: 2px solid #c8c8c8;padding: 6px;')
        else:
            self.pair_mode_clicked_btns.append(n)
            self.check_pair()
            self.pair_mode_clicked_btns = []

    def make_all_btns_white_and_clear_labels(self):
        if self.mode == "Choose pairs":
            self.ui.gridLayoutWidget.show() # pairs_layout
        else:
            self.ui.verticalLayoutWidget.show()  # choose_layout
        self.ui.option_1.setStyleSheet('background: #c8c8c8; border: 1px solid #c8c8c8;padding: 6px;')
        self.ui.option_2.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 6px;')
        self.ui.option_3.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 6px;')
        self.ui.option_4.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 6px;')
        for i in self.pairs_btn_list:
            i.setMinimumHeight(int(self.ui.gridLayoutWidget.height()*0.23))
            #i.setMaximumHeight(int(self.ui.gridLayoutWidget.height()*0.25))
            i.setMinimumWidth(int(self.ui.gridLayoutWidget.width()*0.3))
            i.setStyleSheet('background: #c8c8c8; border: 1px solid #c8c8c8;margin: 1px;')
            i.setEnabled(True)
        self.ui.nextq.hide()
        self.ui.ex_info.setText("")

    def new_question(self):
        self.make_all_btns_white_and_clear_labels()
        self.cell_num = get_random_cell(self.unit, self.q_col)
        self.ui.question.setText(sheets[self.unit][self.q_col + self.cell_num].value.strip())
        options = [self.ui.option_1, self.ui.option_2, self.ui.option_3, self.ui.option_4]
        answers = [self.cell_num]
        self.right_ans = randint(0, 3)
        options[self.right_ans].setText(sheets[self.unit][self.a_col + self.cell_num].value)
        options.pop(self.right_ans)
        for o in options:
            rand_cell_num = get_random_cell(self.unit, self.a_col)
            while rand_cell_num in answers:
                rand_cell_num = get_random_cell(self.unit, self.a_col)
            o.setText(sheets[self.unit][self.a_col + rand_cell_num].value)
            answers.append(rand_cell_num)

    def choosed_option_1(self):
        if self.right_ans == 0:
            self.ui.option_1.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.ui.ex_info.setText(sheets[self.unit][self.ex_col + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_1.setStyleSheet('background: red;border: 1px solid red;padding: 6px;')

    def choosed_option_2(self):
        if self.right_ans == 1:
            self.ui.option_2.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.ui.ex_info.setText(sheets[self.unit][self.ex_col + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_2.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 6px;')

    def choosed_option_3(self):
        if self.right_ans == 2:
            self.ui.option_3.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.ui.ex_info.setText(sheets[self.unit][self.ex_col + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_3.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 6px;')

    def choosed_option_4(self):
        if self.right_ans == 3:
            self.ui.option_4.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 6px;')
            self.ui.ex_info.setText(sheets[self.unit][self.ex_col + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_4.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 6px;')


if __name__ == '__main__':
    start_excel()
    app = QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
