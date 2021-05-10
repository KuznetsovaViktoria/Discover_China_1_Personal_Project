# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choose_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.choose_layout_widget.setGeometry(QtCore.QRect(0, 20, 361, 261))
        self.choose_layout_widget.setObjectName("choose_layout_widget")
        self.choose_layout = QtWidgets.QVBoxLayout(self.choose_layout_widget)
        self.choose_layout.setContentsMargins(0, 0, 0, 0)
        self.choose_layout.setObjectName("choose_layout")
        self.question = QtWidgets.QLabel(self.choose_layout_widget)
        self.question.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(24)
        self.question.setFont(font)
        self.question.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.question.setObjectName("question")
        self.choose_layout.addWidget(self.question)
        self.ex_info = QtWidgets.QLabel(self.choose_layout_widget)
        self.ex_info.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.ex_info.setFont(font)
        self.ex_info.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ex_info.setObjectName("ex_info")
        self.choose_layout.addWidget(self.ex_info)
        self.option_1 = QtWidgets.QPushButton(self.choose_layout_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.option_1.setFont(font)
        self.option_1.setObjectName("option_1")
        self.choose_layout.addWidget(self.option_1)
        self.option_2 = QtWidgets.QPushButton(self.choose_layout_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.option_2.setFont(font)
        self.option_2.setObjectName("option_2")
        self.choose_layout.addWidget(self.option_2)
        self.option_3 = QtWidgets.QPushButton(self.choose_layout_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.option_3.setFont(font)
        self.option_3.setObjectName("option_3")
        self.choose_layout.addWidget(self.option_3)
        self.option_4 = QtWidgets.QPushButton(self.choose_layout_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.option_4.setFont(font)
        self.option_4.setObjectName("option_4")
        self.choose_layout.addWidget(self.option_4)
        self.nextq = QtWidgets.QPushButton(self.centralwidget)
        self.nextq.setGeometry(QtCore.QRect(1, 290, 359, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextq.setFont(font)
        self.nextq.setAcceptDrops(False)
        self.nextq.setAutoFillBackground(False)
        self.nextq.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.nextq.setAutoDefault(False)
        self.nextq.setDefault(False)
        self.nextq.setFlat(False)
        self.nextq.setObjectName("nextq")
        self.main_menu_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_menu_layout_widget.setGeometry(QtCore.QRect(0, 20, 361, 331))
        self.main_menu_layout_widget.setObjectName("main_menu_layout_widget")
        self.main_menu_layout = QtWidgets.QFormLayout(self.main_menu_layout_widget)
        self.main_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.main_menu_layout.setObjectName("main_menu_layout")
        self.label_unit = QtWidgets.QLabel(self.main_menu_layout_widget)
        self.label_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_unit.setObjectName("label_unit")
        self.main_menu_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_unit)
        self.choose_unit = QtWidgets.QSpinBox(self.main_menu_layout_widget)
        self.choose_unit.setMinimum(1)
        self.choose_unit.setMaximum(12)
        self.choose_unit.setObjectName("choose_unit")
        self.main_menu_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.choose_unit)
        self.label_mode = QtWidgets.QLabel(self.main_menu_layout_widget)
        self.label_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mode.setObjectName("label_mode")
        self.main_menu_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_mode)
        self.choose_mode = QtWidgets.QComboBox(self.main_menu_layout_widget)
        self.choose_mode.setObjectName("choose_mode")
        self.main_menu_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.choose_mode)
        self.play_btn = QtWidgets.QPushButton(self.main_menu_layout_widget)
        self.play_btn.setObjectName("play_btn")
        self.main_menu_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.play_btn)
        self.pairs_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.pairs_layout_widget.setGeometry(QtCore.QRect(-1, 19, 361, 261))
        self.pairs_layout_widget.setObjectName("pairs_layout_widget")
        self.pairs_layout = QtWidgets.QGridLayout(self.pairs_layout_widget)
        self.pairs_layout.setContentsMargins(0, 0, 0, 0)
        self.pairs_layout.setSpacing(1)
        self.pairs_layout.setObjectName("pairs_layout")
        self.btn4 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn4.setObjectName("btn4")
        self.pairs_layout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn1.setObjectName("btn1")
        self.pairs_layout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn11 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn11.setObjectName("btn11")
        self.pairs_layout.addWidget(self.btn11, 3, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn2.setObjectName("btn2")
        self.pairs_layout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn10 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn10.setObjectName("btn10")
        self.pairs_layout.addWidget(self.btn10, 3, 0, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn7.setObjectName("btn7")
        self.pairs_layout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn5.setObjectName("btn5")
        self.pairs_layout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn8.setObjectName("btn8")
        self.pairs_layout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn3.setObjectName("btn3")
        self.pairs_layout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn6.setObjectName("btn6")
        self.pairs_layout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn9.setObjectName("btn9")
        self.pairs_layout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btn12 = QtWidgets.QPushButton(self.pairs_layout_widget)
        self.btn12.setObjectName("btn12")
        self.pairs_layout.addWidget(self.btn12, 3, 2, 1, 1)
        self.menu1_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.menu1_layout_widget.setGeometry(QtCore.QRect(-1, 19, 361, 261))
        self.menu1_layout_widget.setObjectName("menu1_layout_widget")
        self.menu1_layout = QtWidgets.QGridLayout(self.menu1_layout_widget)
        self.menu1_layout.setContentsMargins(0, 0, 0, 0)
        self.menu1_layout.setObjectName("menu1_layout")
        self.btn_unit9 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit9.setObjectName("btn_unit9")
        self.menu1_layout.addWidget(self.btn_unit9, 2, 2, 1, 1)
        self.btn_unit3 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit3.setObjectName("btn_unit3")
        self.menu1_layout.addWidget(self.btn_unit3, 0, 2, 1, 1)
        self.btn_unit11 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit11.setObjectName("btn_unit11")
        self.menu1_layout.addWidget(self.btn_unit11, 3, 1, 1, 1)
        self.btn_unit1 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit1.setObjectName("btn_unit1")
        self.menu1_layout.addWidget(self.btn_unit1, 0, 0, 1, 1)
        self.btn_unit7 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit7.setObjectName("btn_unit7")
        self.menu1_layout.addWidget(self.btn_unit7, 2, 0, 1, 1)
        self.btn_unit5 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit5.setObjectName("btn_unit5")
        self.menu1_layout.addWidget(self.btn_unit5, 1, 1, 1, 1)
        self.btn_unit8 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit8.setObjectName("btn_unit8")
        self.menu1_layout.addWidget(self.btn_unit8, 2, 1, 1, 1)
        self.btn_unit6 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit6.setObjectName("btn_unit6")
        self.menu1_layout.addWidget(self.btn_unit6, 1, 2, 1, 1)
        self.btn_unit10 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit10.setObjectName("btn_unit10")
        self.menu1_layout.addWidget(self.btn_unit10, 3, 0, 1, 1)
        self.btn_unit12 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit12.setObjectName("btn_unit12")
        self.menu1_layout.addWidget(self.btn_unit12, 3, 2, 1, 1)
        self.btn_unit4 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit4.setObjectName("btn_unit4")
        self.menu1_layout.addWidget(self.btn_unit4, 1, 0, 1, 1)
        self.btn_unit2 = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_unit2.setObjectName("btn_unit2")
        self.menu1_layout.addWidget(self.btn_unit2, 0, 1, 1, 1)
        self.btn_rad = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_rad.setObjectName("btn_rad")
        self.menu1_layout.addWidget(self.btn_rad, 4, 0, 1, 1)
        self.btn_all = QtWidgets.QPushButton(self.menu1_layout_widget)
        self.btn_all.setObjectName("btn_all")
        self.menu1_layout.addWidget(self.btn_all, 4, 1, 1, 2)
        #self.btn_random = QtWidgets.QPushButton(self.menu1_layout_widget)
        #self.btn_random.setObjectName("btn_random")
        #self.menu1_layout.addWidget(self.btn_random, 4, 2, 1, 1)
        self.menu2_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.menu2_layout_widget.setGeometry(QtCore.QRect(-1, 19, 361, 261))
        self.menu2_layout_widget.setObjectName("menu2_layout_widget")
        self.menu2_layout = QtWidgets.QGridLayout(self.menu2_layout_widget)
        self.menu2_layout.setContentsMargins(0, 0, 0, 0)
        self.menu2_layout.setObjectName("menu2_layout")
        self.pinyin_btn = QtWidgets.QPushButton(self.menu2_layout_widget)
        self.pinyin_btn.setObjectName("pinyin_btn")
        self.menu2_layout.addWidget(self.pinyin_btn, 0, 0, 1, 1)
        self.char_btn = QtWidgets.QPushButton(self.menu2_layout_widget)
        self.char_btn.setObjectName("char_btn")
        self.menu2_layout.addWidget(self.char_btn, 0, 1, 1, 1)
        self.tran_btn = QtWidgets.QPushButton(self.menu2_layout_widget)
        self.tran_btn.setObjectName("tran_btn")
        self.menu2_layout.addWidget(self.tran_btn, 1, 0, 1, 1)
        self.pairs_btn = QtWidgets.QPushButton(self.menu2_layout_widget)
        self.pairs_btn.setObjectName("pairs_btn")
        self.menu2_layout.addWidget(self.pairs_btn, 1, 1, 1, 1)
        self.back_btn = QtWidgets.QPushButton(self.menu2_layout_widget)
        self.back_btn.setObjectName("back_btn")
        self.menu2_layout.addWidget(self.back_btn, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.question.setText(_translate("MainWindow", "TextLabel"))
        self.ex_info.setText(_translate("MainWindow", "TextLabel"))
        self.option_1.setText(_translate("MainWindow", "PushButton"))
        self.option_2.setText(_translate("MainWindow", "PushButton"))
        self.option_3.setText(_translate("MainWindow", "PushButton"))
        self.option_4.setText(_translate("MainWindow", "PushButton"))
        self.nextq.setText(_translate("MainWindow", "Next"))
        self.label_unit.setText(_translate("MainWindow", "Unit:             "))
        self.label_mode.setText(_translate("MainWindow", "Game mode:"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.btn4.setText(_translate("MainWindow", "PushButton"))
        self.btn1.setText(_translate("MainWindow", "PushButton"))
        self.btn11.setText(_translate("MainWindow", "PushButton"))
        self.btn2.setText(_translate("MainWindow", "PushButton"))
        self.btn10.setText(_translate("MainWindow", "PushButton"))
        self.btn7.setText(_translate("MainWindow", "PushButton"))
        self.btn5.setText(_translate("MainWindow", "PushButton"))
        self.btn8.setText(_translate("MainWindow", "PushButton"))
        self.btn3.setText(_translate("MainWindow", "PushButton"))
        self.btn6.setText(_translate("MainWindow", "PushButton"))
        self.btn9.setText(_translate("MainWindow", "PushButton"))
        self.btn12.setText(_translate("MainWindow", "PushButton"))
        self.btn_unit9.setText(_translate("MainWindow", "Unit 9"))
        self.btn_unit3.setText(_translate("MainWindow", "Unit 3"))
        self.btn_unit11.setText(_translate("MainWindow", "Unit 11"))
        self.btn_unit1.setText(_translate("MainWindow", "Unit 1"))
        self.btn_unit7.setText(_translate("MainWindow", "Unit 7"))
        self.btn_unit5.setText(_translate("MainWindow", "Unit 5"))
        self.btn_unit8.setText(_translate("MainWindow", "Unit 8"))
        self.btn_unit6.setText(_translate("MainWindow", "Unit 6"))
        self.btn_unit10.setText(_translate("MainWindow", "Unit 10"))
        self.btn_unit12.setText(_translate("MainWindow", "Unit 12"))
        self.btn_unit4.setText(_translate("MainWindow", "Unit 4"))
        self.btn_unit2.setText(_translate("MainWindow", "Unit 2"))
        self.btn_rad.setText(_translate("MainWindow", "Radicals"))
        self.btn_all.setText(_translate("MainWindow", "All units"))
        #self.btn_random.setText(_translate("MainWindow", "Random unit"))
        self.pinyin_btn.setText(_translate("MainWindow", "Choose pinyin"))
        self.char_btn.setText(_translate("MainWindow", "Choose character"))
        self.tran_btn.setText(_translate("MainWindow", "Choose translation"))
        self.pairs_btn.setText(_translate("MainWindow", "Make pairs"))
        self.back_btn.setText(_translate("MainWindow", "Back"))