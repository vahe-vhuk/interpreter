from IDE_settings.style_sheet import *
from PyQt5.QtWidgets import QPushButton, QLabel
from sys import path
path.append("../")


def inff(self):
    info_btn(self)
    info(self)


def info_btn(self):
    self.info_btn = QPushButton("", self)
    self.info_btn.move(690, 20)
    self.info_btn.resize(80, 100)
    self.info_btn.clicked.connect(lambda: change_info(self))


def change_info(self):
    if self.setting_index == -1:
        self.setting_window.hide()
        self.setting_index *= -1

    if self.help_index == -1:
        self.help_window.hide()
        self.help_index *= -1

    if self.info_index == 1:
        self.info_window.show()
    else:
        self.info_window.hide()
    self.info_index *= -1


def info(self):
    self.info_index = 1
    self.info_window = QLabel("", self)
    self.info_window.setGeometry(20, 140, self.size_width-40, 840)
    self.info_window.hide()
    self.info_window.setStyleSheet(setting_window_style_sheet)
    self.info_window.setStyleSheet(
        'background-image: url("IDE_settings/Capture.PNG")')
