from IDE_settings.style_sheet import *
from PyQt5.QtWidgets import QPushButton, QLabel
from sys import path
path.append("../")


def hell(self):
    help_btn(self)
    helpp(self)


def help_btn(self):
    self.help_btn = QPushButton("", self)
    self.help_btn.move(self.size_width-110, 20)
    self.help_btn.resize(80, 100)
    self.help_btn.clicked.connect(lambda: change_help(self))


def change_help(self):
    if self.info_index == -1:
        self.info_window.hide()
        self.info_index *= -1

    if self.setting_index == -1:
        self.setting_window.hide()
        self.setting_index *= -1

    if self.help_index == 1:
        self.help_window.show()
    else:
        self.help_window.hide()
    self.help_index *= -1


def helpp(self):
    self.help_index = 1
    self.help_window = QLabel("", self)
    self.help_window.setGeometry(20, 140, self.size_width-40, 840)
    self.help_window.hide()
    self.help_window.setStyleSheet(setting_window_style_sheet)
