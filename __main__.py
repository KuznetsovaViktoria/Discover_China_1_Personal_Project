from random import *
import PyQt5
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QPalette, QImage, QBrush

from mydesignDONOTCHANGE import Ui_MainWindow
import sys
import openpyxl
from PyQt5.QtWidgets import *
from functools import partial
from threading import Timer


def start_excel():
    global sheets
    wb = openpyxl.load_workbook(filename="C:\Programming\Discover China\Discover China 1 all vocabulary.xlsx")
    sheets = [wb['unit 1'], wb['unit 2'], wb['unit 3'], wb['unit 4'], wb['unit 5'], wb['unit 6'],
              wb['unit 7'], wb['unit 8'], wb['unit 9'], wb['unit 10'], wb['unit 11'], wb['unit 12'], wb['radicals']]


def get_random_cell(unit, q_col):
    cell_num = str(randint(1, 150))
    cell = sheets[unit][q_col + cell_num]
    while cell.value == '' or cell.value is None:
        cell_num = str(randint(1, 150))
        cell = sheets[unit][q_col + cell_num]
    return cell_num


class mywindow(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        '''oImage = QImage("background.jpg")
        sImage = oImage.scaled(QSize(self.height(), self.width()))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)'''
        #self.setStyleSheet('.QWidget {background-image: url(background.jpg);}')
        self.question_list = [self.ui.question, self.ui.ex_info, self.ui.option_1, self.ui.option_2, self.ui.option_3,
                              self.ui.option_4]
        self.pairs_btn_list = [self.ui.btn1, self.ui.btn2, self.ui.btn3, self.ui.btn4, self.ui.btn5, self.ui.btn6,
                               self.ui.btn7, self.ui.btn8, self.ui.btn9, self.ui.btn10, self.ui.btn11, self.ui.btn12]
        self.menu1_btn_list = [self.ui.btn_unit1, self.ui.btn_unit2, self.ui.btn_unit3, self.ui.btn_unit4,
                               self.ui.btn_unit5, self.ui.btn_unit6, self.ui.btn_unit7, self.ui.btn_unit8,
                               self.ui.btn_unit9, self.ui.btn_unit10, self.ui.btn_unit11, self.ui.btn_unit12,
                               self.ui.btn_rad, self.ui.btn_all, self.ui.btn_random]
        self.menu2_btn_list = [self.ui.pinyin_btn, self.ui.char_btn, self.ui.tran_btn, self.ui.pairs_btn,
                               self.ui.back_btn]
        self.made_pairs = []   # what pairs has been made in pair mode
        self.pair_mode_clicked_btns = []    # what buttons has been clicked in pair mode
        self.cell_num = 0  # cell number with the right answer
        self.right_ans = None  # the answer
        self.unit = 1  # choosed unit
        self.mode = "Choose pinyin"
        self.q_col = 'A'  # column in the excel table, from where we take questions, depends on the choosed mode
        self.a_col = 'B'  # column in the excel table, from where we take answers, depends on the choosed mode
        self.ex_col = 'C'  # the third column to show full information about the word after the right answer
        self.ui.nextq.setStyleSheet('background: #86f353; border: 1px solid #86f353;padding: 3px; margin: 2px;;')
        #self.ui.centralwidget.setStyleSheet('background: white')
        self.ui.question.setFont(QFont('SimSun', 24))
        for i in self.question_list[1:]:
            i.setFont(QFont('SimSun', 18))

        self.ui.question.adjustSize()
        self.ui.ex_info.adjustSize()

        self.ui.choose_mode.addItem("Choose pinyin")
        self.ui.choose_mode.addItem("Choose character")
        self.ui.choose_mode.addItem("Choose translation")
        self.ui.choose_mode.addItem("Make pairs")
        self.ui.choose_mode.addItem("Choose radicals")

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
        for i in range(15):
            self.menu1_btn_list[i].clicked.connect(partial(self.menu1_clicked, i))
        for i in range(5):
            self.menu2_btn_list[i].clicked.connect(partial(self.menu2_clicked, self.menu2_btn_list[i].text))

        self.beginning()
        self.setWindowTitle("Discover China 1")
        self.resize(550, 600)
        self.resized.connect(self.resizing)

    def beginning(self):
        self.hide_question()
        self.ui.main_menu_layout_widget.hide()
        self.ui.menu2_layout_widget.hide()
        self.ui.menu1_layout_widget.show()

    def menu1_clicked(self, n):
        if n < 12:
            self.unit = n
        elif n == 12:
            self.unit = 12
        else:
            self.unit = randint(0, 11)
        self.ui.menu2_layout_widget.show()
        self.ui.menu1_layout_widget.hide()

    def menu2_clicked(self, t):
        print(t)
        if t != 'Back':
            self.onActivated_choosing_mode(t)
        else:
            self.beginning()

    def start_playing(self):
        '''if self.mode == "Choose radicals":
            self.unit = 12
        else:
            self.unit = int(self.ui.choose_unit.value()) - 1'''
        self.ui.main_menu_layout_widget.hide()
        if self.mode == "Make pairs":
            self.ui.pairs_layout_widget.show()
            self.new_pair_question()
        else:
            self.ui.choose_layout_widget.show()
            self.new_question()

    def next_question(self):
        if self.mode == "Make pairs":
            self.new_pair_question()
        else:
            self.new_question()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(mywindow, self).resizeEvent(event)

    def resizing(self):
        self.ui.main_menu_layout_widget.setGeometry(QtCore.QRect(0, 20, self.width(), self.height()))
        self.ui.choose_layout_widget.setGeometry(QtCore.QRect(0, 20, self.width(), int(self.height()*0.66)))
        self.ui.pairs_layout_widget.setGeometry(QtCore.QRect(0, 20, self.width(), int(self.height()*0.63)))
        self.ui.menu1_layout_widget.setGeometry(QtCore.QRect(0, 20, self.width(), int(self.height()*0.75)))
        self.ui.menu2_layout_widget.setGeometry(QtCore.QRect(0, 20, self.width(), int(self.height()*0.75)))

        for w in self.question_list:
            w.setMinimumSize(QtCore.QSize(0, int(self.height()*0.1)))
        self.ui.nextq.setGeometry(QtCore.QRect(1, int(self.height()*0.7), self.width(), int(self.height()*0.11)))


    def onActivated_choosing_mode(self, mode):
        if mode == "Choose pinyin":
            self.mode = "Choose pinyin"
            self.q_col = 'A'
            self.a_col = 'B'
            self.ex_col = 'C'
        elif mode == "Choose character":
            self.mode = "Choose character"
            self.q_col = 'C'
            self.a_col = 'A'
            self.ex_col = 'B'

        elif mode == "Choose translation":
            self.mode = "Choose translation"
            self.q_col = 'A'
            self.a_col = 'C'
            self.ex_col = 'B'
        elif mode == "Make pairs":
            self.mode = "Make pairs"
        elif mode == "Choose radicals":
            self.mode = "Choose radicals"
            self.q_col = 'A'
            self.a_col = 'C'
            self.ex_col = 'B'
            for i in self.question_list[2:]:
                i.setFont(QFont('Calibri', 14))
        if mode != "Choose radicals":
            for i in self.question_list[2:]:
                i.setFont(QFont('SimSun', 18))

    def hide_question(self):
        self.ui.choose_layout_widget.hide()
        self.ui.pairs_layout_widget.hide()
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
            self.pairs_btn_list[i[1]].setFont(QFont('SimSun', 20 - int(0.6*len(self.pairs_btn_list[i[1]].text()))))
            #self.pairs_btn_list[i[0]].styleSheet('font-weight: normal')
            #self.pairs_btn_list[i[1]].styleSheet('font-weight: bold')

    def check_pair(self):
        a = self.pair_mode_clicked_btns[0]
        b = self.pair_mode_clicked_btns[1]
        if [a, b] in self.right_ans or [b, a] in self.right_ans:
            self.made_pairs.append(a)
            self.made_pairs.append(b)
            self.pairs_btn_list[a].setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 3px; margin: 2px;;')
            self.pairs_btn_list[b].setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 3px; margin: 2px;;')
            self.pairs_btn_list[a].setEnabled(False)
            self.pairs_btn_list[b].setEnabled(False)
        else:
            self.pairs_btn_list[a].setStyleSheet('background: red;border: 1px solid red;padding: 3px; margin: 2px;;')
            self.pairs_btn_list[b].setStyleSheet('background: red;border: 1px solid red;padding: 3px; margin: 2px;;')
            t = Timer(1, self.pair_mode_change_btn_color_to_white, args=[a, b], kwargs=None)
            t.start()
        if len(self.made_pairs) == 12:
            self.ui.nextq.show()

    def pair_mode_change_btn_color_to_white(self, *n):
        for i in n:
            self.pairs_btn_list[i].setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 3px; margin: 2px;;')

    def btn_pair_mode_been_clicked(self, n):
        if self.pair_mode_clicked_btns == []:
            self.pair_mode_clicked_btns.append(n)
            self.pairs_btn_list[n].setStyleSheet('background: #c8c8c8;border: 2px solid black;padding: 3px; margin: 2px;;')
        elif self.pair_mode_clicked_btns == [n]:
            self.pair_mode_clicked_btns = []
            self.pairs_btn_list[n].setStyleSheet('background: #c8c8c8;border: 2px solid #c8c8c8;padding: 3px; margin: 2px;;')
        else:
            self.pair_mode_clicked_btns.append(n)
            self.check_pair()
            self.pair_mode_clicked_btns = []

    def make_all_btns_white_and_clear_labels(self):
        if self.mode == "Make pairs":
            self.ui.pairs_layout_widget.show()
        else:
            self.ui.choose_layout_widget.show()
        self.ui.option_1.setStyleSheet('background: #c8c8c8; border: 1px solid #c8c8c8;padding: 3px; margin: 2px;;')
        self.ui.option_2.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 3px; margin: 2px;;')
        self.ui.option_3.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 3px; margin: 2px;;')
        self.ui.option_4.setStyleSheet('background: #c8c8c8;border: 1px solid #c8c8c8;padding: 3px; margin: 2px;;')
        for i in self.pairs_btn_list:
            i.setMinimumHeight(int(self.ui.pairs_layout_widget.height()*0.23))
            i.setMinimumWidth(int(self.ui.pairs_layout_widget.width()*0.3))
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
            self.ui.option_1.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 3px; margin: 2px;;')
            self.ui.ex_info.setText(sheets[self.unit][self.ex_col + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_1.setStyleSheet('background: red;border: 1px solid red;padding: 3px; margin: 2px;;')

    def choosed_option_2(self):
        if self.right_ans == 1:
            self.ui.option_2.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 3px; margin: 2px;;')
            self.ui.ex_info.setText(sheets[self.unit][self.ex_col + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_2.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 3px; margin: 2px;;')

    def choosed_option_3(self):
        if self.right_ans == 2:
            self.ui.option_3.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 3px; margin: 2px;;')
            self.ui.ex_info.setText(sheets[self.unit][self.ex_col + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_3.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 3px; margin: 2px;;')

    def choosed_option_4(self):
        if self.right_ans == 3:
            self.ui.option_4.setStyleSheet('background: #86f353;border: 1px solid #86f353;padding: 3px; margin: 2px;;')
            self.ui.ex_info.setText(sheets[self.unit][self.ex_col + self.cell_num].value)
            self.ui.nextq.show()
        else:
            self.ui.option_4.setStyleSheet('background: rgb(255,0,0);border: 1px solid red;padding: 3px; margin: 2px;;')


if __name__ == '__main__':
    start_excel()
    app = QApplication([])
    app.setStyle('Fusion')
    #print(PyQt5.QtWidgets.QStyleFactory.keys())
    application = mywindow()
    application.show()

    sys.exit(app.exec())
