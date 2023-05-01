from sys import path
path.append("../")
from PyQt5.QtWidgets import QLabel,QPushButton,QGraphicsDropShadowEffect
from IDE_settings.style_sheet import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



def sett(self):
	self.style_name = "style_1"
	self.style_index = 0
	setting_btn(self)
	settings(self)
	chenge_style(self)



def setting_btn(self):
	self.setting_btn = QPushButton("",self)
	self.setting_btn.move(580,20)
	self.setting_btn.resize(80,100)
	self.setting_btn.clicked.connect(lambda: change_settings(self))


def settings(self):
	self.setting_index = 1
	self.setting_window = QLabel("",self)
	self.setting_window.setGeometry(20,140,self.size_width-40,840)
	self.setting_window.setStyleSheet(setting_window_style_sheet)
	shadow = QGraphicsDropShadowEffect()
	shadow.setBlurRadius(25)
	self.setting_window.setGraphicsEffect(shadow)
	self.setting_window.setAlignment(Qt.AlignHCenter)
	self.setting_window.hide()

	self.set_btn_1 = QPushButton("",self.setting_window)
	self.set_btn_1.setGeometry(40,8,480,270)
	self.set_btn_1.setStyleSheet('background-image:url("IDE_settings/style_1/style_button.png")')
	self.set_btn_1.pressed.connect(lambda: set_style(self,"style_1"))

	self.set_btn_2 = QPushButton("",self.setting_window)
	self.set_btn_2.setGeometry(40,285,480,270)
	self.set_btn_2.setStyleSheet('background-image:url("IDE_settings/style_2/style_button.png")')
	self.set_btn_2.pressed.connect(lambda: set_style(self,"style_2"))

	self.set_btn_3 = QPushButton("",self.setting_window)
	self.set_btn_3.setGeometry(40,562,480,270)
	self.set_btn_3.setStyleSheet('background-image:url("IDE_settings/style_3/style_button.png")')
	self.set_btn_3.pressed.connect(lambda: set_style(self,"style_3"))


	self.set_btn_4 = QPushButton("",self.setting_window)
	self.set_btn_4.setGeometry(self.size_width-560,8,480,270)
	self.set_btn_4.setStyleSheet('background-image:url("IDE_settings/style_4/style_button.png")')
	self.set_btn_4.pressed.connect(lambda: set_style(self,"style_4"))


	self.set_btn_5 = QPushButton("",self.setting_window)
	self.set_btn_5.setGeometry(self.size_width-560,285,480,270)
	self.set_btn_5.setStyleSheet('background-image:url("IDE_settings/style_5/style_button.png")')
	self.set_btn_5.pressed.connect(lambda: set_style(self,"style_5"))

	self.set_btn_6 = QPushButton("",self.setting_window)
	self.set_btn_6.setGeometry(self.size_width-560,562,480,270)
	self.set_btn_6.setStyleSheet('background-image:url("IDE_settings/style_6/style_button.png")')
	self.set_btn_6.pressed.connect(lambda: set_style(self,"style_6"))

	f = open("IDE_settings/style_control.txt","r")
	q = f.read().splitlines()
	f.close()

	self.code_font_lable = QLabel("Text Font Size\noutput<<~Hello World!>>",self.setting_window)
	self.code_font_lable.setGeometry(530,135,820,270)
	self.code_font_lable.setFont(QFont("rockwell",int(q[1])))
	self.code_font_lable.setAlignment(Qt.AlignCenter)
	self.code_font_lable.setStyleSheet('background-image:url("bhjjn");border:0px;')



	self.term_font_lable = QLabel("Terminal Font Size\nHello World!",self.setting_window)
	self.term_font_lable.setGeometry(530,420,820,270)
	self.term_font_lable.setFont(QFont("rockwell",int(q[2])))
	self.term_font_lable.setAlignment(Qt.AlignCenter)
	self.term_font_lable.setStyleSheet('background-image:url("bhjjn");border:0px;')



	self.code_font_increment_btn = QPushButton(str(int(q[1])+1),self.code_font_lable)
	self.code_font_increment_btn.setGeometry(710,80,110,110)
	self.code_font_increment_btn.setStyleSheet(code_font_style_sheet)
	self.code_font_increment_btn.pressed.connect(lambda: text_font(self,1))

	self.code_font_decrement_btn = QPushButton(str(int(q[1])-1),self.code_font_lable)
	self.code_font_decrement_btn.setGeometry(20,80,110,110)
	self.code_font_decrement_btn.setStyleSheet(code_font_style_sheet)
	self.code_font_decrement_btn.pressed.connect(lambda: text_font(self,-1))


	self.term_font_increment_btn = QPushButton(str(int(q[2])+1),self.term_font_lable)
	self.term_font_increment_btn.setGeometry(710,80,110,110)
	self.term_font_increment_btn.setStyleSheet(code_font_style_sheet)
	self.term_font_increment_btn.pressed.connect(lambda: term_font(self,1))


	self.term_font_decrement_btn = QPushButton(str(int(q[2])-1),self.term_font_lable)
	self.term_font_decrement_btn.setGeometry(20,80,110,110)
	self.term_font_decrement_btn.setStyleSheet(code_font_style_sheet)
	self.term_font_decrement_btn.pressed.connect(lambda: term_font(self,-1))



def change_settings(self):
	if self.info_index == -1:
		self.info_window.hide()
		self.info_index *= -1
	
	if self.help_index == -1:
		self.help_window.hide()
		self.help_index *= -1

	if self.setting_index == 1:
		self.setting_window.show()
	else:
		self.setting_window.hide()
	self.setting_index *= -1

def chenge_style(self):
	if self.style_index == 0:
		f = open("IDE_settings/style_control.txt","r")
		q = f.read().splitlines()
		f.close()
		for i in range(len(style_sheet_list)):
			k = style_sheet_list[i].split(self.style_name)
			style_sheet_list[i] = k[0] + q[0] + k[1]
		self.style_name = q[0]
		self.style_index += 1
	self.open_file_btn.setStyleSheet(style_sheet_list[0])
	self.save_file_btn.setStyleSheet(style_sheet_list[1])
	self.save_as_file_btn.setStyleSheet(style_sheet_list[2])
	self.run_file_btn.setStyleSheet(style_sheet_list[3])
	self.debug_btn.setStyleSheet(style_sheet_list[4])
	self.setting_btn.setStyleSheet(style_sheet_list[5])
	self.info_btn.setStyleSheet(style_sheet_list[6])
	self.help_btn.setStyleSheet(style_sheet_list[7])
	if self.doc_btn_list:
		for i in range(len(self.doc_btn_list)):
			self.doc_btn_list[i].setStyleSheet(style_sheet_list[8])
	self.lable1.setStyleSheet(style_sheet_list[9])
	self.lable2.setStyleSheet(style_sheet_list[10])
	self.setStyleSheet(style_sheet_list[11])
	self.textbox.setStyleSheet(style_sheet_list[12])
	self.answer_box.setStyleSheet(style_sheet_list[13])

def set_style(self,style_n):
	if style_n != self.style_name:
		for i in range(len(style_sheet_list)):
			k = style_sheet_list[i].split(self.style_name)
			style_sheet_list[i] = k[0] + style_n + k[1]
		f = open("IDE_settings/style_control.txt","w")
		f.write(style_n+"\n"+str(self.text_font_size) + "\n" + str(self.term_font_size))
		f.close()
		chenge_style(self)
		self.style_name = style_n

def text_font(self,arg):
	if 0 < self.text_font_size+arg < 51:
		self.text_font_size += arg
		self.code_font_increment_btn.setText(str(self.text_font_size+1))
		self.code_font_decrement_btn.setText(str(self.text_font_size-1))
		self.textbox.setFont(QFont("arial",self.text_font_size))
		self.code_font_lable.setFont(QFont("rockwell",self.text_font_size))
		f = open("IDE_settings/style_control.txt","w")
		f.write(self.style_name + "\n" + str(self.text_font_size) + "\n" + str(self.term_font_size))
		f.close()

def term_font(self,arg):
	if 0 < self.term_font_size+arg < 51:
		self.term_font_size += arg
		self.term_font_increment_btn.setText(str(self.term_font_size+1))
		self.term_font_decrement_btn.setText(str(self.term_font_size-1))
		self.answer_box.setFont(QFont("arial",self.term_font_size))
		self.term_font_lable.setFont(QFont("rockwell",self.term_font_size))
		f = open("IDE_settings/style_control.txt","w")
		f.write(self.style_name + "\n" + str(self.text_font_size) + "\n" + str(self.term_font_size))
		f.close()