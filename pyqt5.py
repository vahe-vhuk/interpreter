from IDE_settings.style_sheet import *

from ctypes import windll
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from types import GeneratorType
from time import sleep


from properties.settings import sett, text_font, change_settings
from properties.info import inff, change_info
from properties.help import hell, change_help
from properties.syntax_highlihter import Highlighter


class inter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.work_space()
        self.initUI()

    def work_space(self):
        self.size_height = windll.user32.GetSystemMetrics(1) - 70
        self.size_width = windll.user32.GetSystemMetrics(0)
        self.setMinimumHeight(self.size_height)
        self.setMinimumWidth(self.size_width)
        self.move(0, 0)
        self.setWindowTitle("interpreter")
        self.setWindowIcon(QIcon("IDE_settings/icon.PNG"))
        self.line_count = 0
        self.symbol_count = 0
        self.highlight_flag = -1

        self.document_list = []
        self.doc_btn_list = []
        self.work_file_name = ""

        self.lables()

        self.text_boxes()

        self.open_file_btn()
        self.save_file_btn()
        self.save_as_file_btn()
        self.run_file_btn()
        self.debug_btn()
        hell(self)
        inff(self)
        sett(self)

    def text_boxes(self):
        f = open("IDE_settings/style_control.txt", "r")
        q = f.read().splitlines()
        f.close()
        self.textbox = QPlainTextEdit(self)
        self.textbox.highlighter = Highlighter(self.textbox.document())

        self.textbox.setGeometry(190, 140, self.size_width-210, 660)
        self.textbox.setFont(QFont("arial", int(q[1])))
        self.text_font_size = int(q[1])
        self.textbox.setTabStopWidth(4 * self.textbox.fontMetrics().width(' '))
        self.textbox.show()

        self.answer_box = QPlainTextEdit(self)
        self.answer_box.setGeometry(190, 810, self.size_width - 210, 170)
        self.answer_box.setFont(QFont("arial", int(q[2])))
        self.term_font_size = int(q[2])

    def lables(self):

        self.lable1 = QLabel("", self)
        self.lable1.setGeometry(20, 10, self.size_width-40, 120)
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(7)
        self.lable1.setGraphicsEffect(shadow1)

        self.lable2 = QLabel("", self)
        self.lable2.setGeometry(20, 140, 160, 840)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(7)
        self.lable2.setGraphicsEffect(shadow2)

        self.lable3 = QLabel(str(self.line_count)+" lines" +
                             "   " + str(self.symbol_count)+" symbols", self)
        self.lable3.setGeometry(0, self.size_height-15, self.size_width, 20)
        self.lable3.setStyleSheet(lable3_style_sheet)

        self.mini_labels()

    def mini_labels(self):
        for i in range(7):
            self.g = QLabel("", self.lable1)
            self.g.setGeometry(110*i, 0, 100, 120)
            self.g.setStyleSheet(mini_lables_style_sheet)
            self.k = QLabel("", self.g)
            self.k.setGeometry(7, 17, 86, 86)
            self.k.setStyleSheet(macro_lables_style_sheet)

        wi = self.lable1.frameGeometry().width()

        self.g = QLabel("", self.lable1)
        self.g.setGeometry(wi-100, 0, 100, 120)
        self.g.setStyleSheet(mini_lables_style_sheet)

        self.k = QLabel("", self.g)
        self.k.setGeometry(7, 17, 86, 86)
        self.k.setStyleSheet(macro_lables_help_style_sheet)

    def open_file_btn(self):
        self.open_file_btn = QPushButton("", self)
        self.open_file_btn.move(30, 20)
        self.open_file_btn.resize(80, 100)
        self.open_file_btn.clicked.connect(self.open_file)

    def save_file_btn(self):
        self.save_file_btn = QPushButton("", self)
        self.save_file_btn.move(140, 20)
        self.save_file_btn.resize(80, 100)
        self.save_file_btn.clicked.connect(self.save_file)

    def save_as_file_btn(self):
        self.save_as_file_btn = QPushButton("", self)
        self.save_as_file_btn.move(250, 20)
        self.save_as_file_btn.resize(80, 100)
        self.save_as_file_btn.clicked.connect(self.save_as_file)

    def run_file_btn(self):
        self.run_file_btn = QPushButton("", self)
        self.run_file_btn.move(360, 20)
        self.run_file_btn.resize(80, 100)

    def debug_btn(self):
        self.debug_btn = QPushButton("", self)
        self.debug_btn.move(470, 20)
        self.debug_btn.resize(80, 100)

    def open_file(self):
        fil = QFileDialog.getOpenFileName(
            self, "open file", "", "VHUK file (*.vah)")
        name = fil[0].split("/")[-1]
        if (fil[0] and len(self.doc_btn_list) < 20 and
                fil[0] not in self.document_list):
            self.document_list.append(fil[0])
            self.doc_btn_list.append(QPushButton(name, self.lable2))

            self.doc_btn_list[-1].setGeometry(10, 10 +
                                              41*(len(self.doc_btn_list)-1)+1,
                                              140, 40)
            self.doc_btn_list[-1].setStyleSheet(style_sheet_list[8])
            self.doc_btn_list[-1].setFont(QFont("Arial", 13))
            self.doc_btn_list[-1].show()
            self.doc_btn_list[-1].clicked.connect(
                lambda: self.open_file_b(fil[0]))
            self.open_file_b(fil[0])

    def open_file_b(self, fil):

        self.work_file_name = fil
        try:
            f = open(fil, "r")
            q = f.read()
            f.close()
            self.symbol_count = len(q)
            self.line_count = len([i for i in q.splitlines() if i != ""])
            self.lable3.setText(str(self.line_count)+" lines" +
                                "   "+str(self.symbol_count)+" symbols")
            self.textbox.setPlainText(q)
            self.setWindowTitle("interpreter -- "+fil.split("/")[-1])
        except(FileNotFoundError):
            tmp = str(self.work_file_name.split("/")[-1])
            self.answer_box.appendPlainText("\nfile " + tmp + " was deleted")

    def save_file(self):
        if self.work_file_name:
            f = open(self.work_file_name, "w")
            f.write(self.textbox.toPlainText())
            f.close()
            f = open(self.work_file_name, "r")
            q = f.read()
            f.close()
            self.symbol_count = len(q)
            self.line_count = len([i for i in q.splitlines() if i != ""])
            self.lable3.setText(str(self.line_count)+" lines" +
                                "   "+str(self.symbol_count)+" symbols")

    def save_as_file(self):
        res = QFileDialog.getSaveFileName(
            self, "save", "", "VHUK file (*.vah)")
        if res[0]:
            f = open(res[0], "w")
            f.write(self.textbox.toPlainText())
            f.close()

    def run_file(self):
        pass

    def initUI(self):

        open_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        open_shortcut.activated.connect(self.open_file)

        save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        save_shortcut.activated.connect(self.save_file)

        save_as_shortcut = QShortcut(QKeySequence("Ctrl+Shift+S"), self)
        save_as_shortcut.activated.connect(self.save_as_file)

        run_file_shortcut = QShortcut(QKeySequence("Ctrl+B"), self)
        run_file_shortcut.activated.connect(self.run_file)

        help_shortcat = QShortcut(QKeySequence("Ctrl+H"), self)
        help_shortcat.activated.connect(lambda: change_help(self))

        setting_shortcat = QShortcut(QKeySequence("Ctrl+P"), self)
        setting_shortcat.activated.connect(lambda: change_settings(self))

        info_shortcat = QShortcut(QKeySequence("Ctrl+I"), self)
        info_shortcat.activated.connect(lambda: change_info(self))

        font_size_inc_shortcut = QShortcut(QKeySequence("Ctrl+Up"), self)
        font_size_inc_shortcut.activated.connect(lambda: text_font(self, 1))

        font_size_dec_shortcut = QShortcut(QKeySequence("Ctrl+Down"), self)
        font_size_dec_shortcut.activated.connect(lambda: text_font(self, -1))
