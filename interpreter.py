from arifmetic.test import recurs_arifmetic,find_type,functions_dict,functions_argumens_dict
from arifmetic.BoolArifmetik import recurs_bool_arifmetic
from intergatet_functions.lists import list_function_names,list_func
from intergatet_functions.dicts import dict_function_names,dict_func
from intergatet_functions.strings import string_function_names, string_func
import sys
from PyQt5.QtWidgets import QApplication,QInputDialog,QLineEdit,QMenu,QSystemTrayIcon
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QIcon
from pyqt5 import inter

# import pyautogui as pg
sys.path.append(".")

right_code_line_start = """abcdefghijklmnopqrstuvwxyz
						   ABCDEFGHIJKLMNOPQRSTUVWXYZ"""


debug_list_1 = ['+','-','*','/','//','%','<','>','<=','>=','||','&&','==','!=','**','=']
debug_list_2 = ['if','else','for','while','return',',','func']





def correct_name(arg):
	print(arg)
	for i in range(48):
		if chr(i) in arg:
			return False
	for i in range(58,65):
		if chr(i) in arg:
			return False
	for i in range(91,97):
		if chr(i) in arg and i != 95:
			return False
	for i in range(123,128):
		if chr(i) in arg:
			return False
	for i in range(48,58):
		if chr(i) == arg[0]:
			return False
	return True


def preprocessor(code):
	code = code.replace("{","<<").replace("}",">>").splitlines()
	code_list = [p for p in code if p != ""]
	code_list = [p for p in code_list if p[0] != "#"]
	for d in range(2):
		if code_list[d][:8] == "include ":
			modul_name_list = code_list[d][8:].split(", ")
			for moduls in modul_name_list:
				print(moduls)
				modul = open(moduls + ".vah","r")
				modul_code = modul.read()
				modul.close()
				modul_code_list = preprocessor(modul_code)
				print(modul_code_list)
				code_list[d:d+1] = modul_code_list
				print(4634634163516351351653165)
				print(code_list)
	return code_list	




class interpr(inter):
	def __init__(self):
		super().__init__()
		self.run_file_btn.clicked.connect(self.run_file)
		self.debug_btn.clicked.connect(self.debuger)



	#Interpreter code
	##############################################################################################################################
	def interprete(self,code_list,variable_dict = {}):
		R = len(code_list)
		d = 0
		while d < R:
			print(code_list, "\n")
			t = code_list[d].split(" = ")
	##############################################################################################################################
			if "=" not in code_list[d] and "'" in code_list[d]:
				find_type(code_list[d],variable_dict)
			if code_list[d] == "...":
				d -= 1
				continue

	#code for include moduls
	##############################################################################################################################
			# if code_list[d][:8] == "include ":
			# 	modul_name_list = code_list[d][8:].split(", ")
			# 	for moduls in modul_name_list:
			# 		print(moduls)
			# 		modul = open(moduls + ".vah","r")
			# 		modul_code = modul.read()
			# 		modul.close()
			# 		modul_code_list = preprocessor(modul_code)
			# 		print(modul_code_list)
			# 		code_list[d:d+1] = modul_code_list
			# 		print(4634634163516351351653165)
			# 		print(code_list)
			# 	d += 1
			# 	continue

	##############################################################################################################################



	#code for IF-ELSE block
	##############################################################################################################################
			if code_list[d][:2] == "if" and code_list[d][-1] == "|":
				k = recurs_bool_arifmetic(code_list[d][3:-1],variable_dict)
				T = []
				for a in code_list[d:]:
					if a[:1] != "\t" and a[:5] != "else|" and a[:2] != "if":
						break
					T.append(a)
				E = len(T)
				index = -1
				for ind in range(E):
					if T[ind] == "else|":
						index = ind
						break
				T = [a[1:] for a in T]
				if index != -1:
					time_list = T[1:index] if k else T[index+1:]
					code_list[d:d+E] = time_list
					R += len(time_list)-E
					# l = self.interprete(T[1:index],variable_dict) if k else self.interprete(T[index+1:],variable_dict)
				elif index == -1 and k:
					code_list[d:d+E] = T
				# 	l = self.interprete(T,variable_dict)
				# if l != None:
				# 	return l
				# d += E
				continue
	##############################################################################################################################

	#Code for while loop
	##############################################################################################################################
			whil = len(code_list[d])
			if whil > 4 and code_list[d][:5] == "while" and code_list[d][-1] == "|":
				u = code_list[d][6:-1]
				W = []
				for a in code_list[d+1:]:
					if a[:1] != "\t":
						break
					W.append(a[1:])
				E = len(W)
				while True:
					rec = recurs_bool_arifmetic(u,variable_dict)
					if not rec:
						break
					l = self.interprete(W,variable_dict)
					if l != None:
						return l
				d += E	
	##############################################################################################################################


	#Code for FOR loop  for i = 1 downto n|
	##############################################################################################################################
			if whil > 14 and code_list[d][:3] == "for" and code_list[d][-1] == "|":
				u = code_list[d][:-1].split(" ")[1:]
				s = find_type(u[2])
				s = s if isinstance(s,int) else variable_dict[s]
				variable_dict[u[0]] = s
				v1,v2 = " == ",0
				if u[-2] == "to":
					v1,v2 = " <= ",1
				elif u[-2] == "downto":
					v1,v2 = " >= ",-1
				u2 = str(u[0]) + v1 + str(u[-1])
				W = []
				for a in code_list[d+1:]:
					if a[:1] != "\t":
						break
					W.append(a[1:])
				E = len(W)
				while True:
					rec = recurs_bool_arifmetic(u2,variable_dict)
					if not rec:
						break
					l = self.interprete(W,variable_dict)
					if l != None:
						return None
					variable_dict[u[0]] += v2
				variable_dict.pop(u[0])
				d += E
	##############################################################################################################################

	#Code for functions
	##############################################################################################################################
			if code_list[d][:4] == "func" and code_list[d][-1] == "|":
				if "<<" in code_list[d] and ">>" in code_list[d]:
					if code_list[d][5] in  right_code_line_start:
						functions_name = code_list[d][5:code_list[d].index("<<")]
						argument_names = (code_list[d].split("<<")[1].split(">>")[0].split(","))
						W = [argument_names]
						for a in code_list[d+1:]:
							if a[:1] != "\t":
								break
							W.append(a[1:])
						E = len(W) - 1
						functions_dict[functions_name] = W
						d += E
			if code_list[d][:6] == "return":
				return recurs_arifmetic(code_list[d][7:],variable_dict)

	##############################################################################################################################


	#Code for variable resolution
	##############################################################################################################################
			# print(t)
			if len(t) == 2:
				arif = t[1]
				fffff = arif.split("<<")[0]
				# if not correct_name(t[0]):
				# 	raise NameError("Uncorrect variable name")

				if "<<" in code_list[d] and ">>" in code_list[d] and fffff == "input":
					l = arif.split("<<")[1].split(">>")[0]
					if l[0] != "~":
						raise SyntaxError("Argument in function input<<>> must have type string")
					res = QInputDialog.getText(self,"Input",l[1:])
					if not res[1]:
						raise ValueError("ababbaba")
					f = find_type(res[0])
					if isinstance(f,str):
						f = "~" + f
					variable_dict[t[0]] = f

				elif "<<" in code_list[d] and ">>" in code_list[d] and fffff in functions_dict:
					find_type(arif,variable_dict)
					print(functions_dict,functions_argumens_dict)
					variable_dict[t[0]] = self.interprete(functions_dict[fffff][1:],functions_argumens_dict[fffff])
				else:
					variable_dict[t[0]] = recurs_arifmetic(arif,variable_dict)
	##############################################################################################################################


		
	#code for output operation
	##############################################################################################################################
			if code_list[d][:8] == "output<<" and code_list[d][-2:] == ">>":
				r = [code_list[d][8:-2].split(", ")]
				r = r[0]
				for i in r:
					e = recurs_arifmetic(i,variable_dict) if i[0] != "~" else i
					if isinstance(e,str):
						if e[0] == " ":
							e = e[1:]
						if e[0] == "~":
							e = e[1:]
						# else:
						# 	raise ValueError("Variable  " + e + "  Not found")
					print(e,end=" ")
					txet = self.answer_box.toPlainText()
					txet += str(e) + " "
					self.answer_box.setPlainText(txet)
				print()
				self.answer_box.appendPlainText("")				
	##############################################################################################################################
			d += 1
		
		return None

	def run_file(self):
		print("dfghjkjhgfghj")
		self.answer_box.setPlainText("")
		try:
			self.answer_box.setPlainText("")
			if self.work_file_name:
				f = open(self.work_file_name,"r")
				code = f.read()
				f.close()
				# code = code.replace("{","<<").replace("}",">>").splitlines()
				# code_list = [p for p in code if p != ""]
				# code_list = [p for p in code_list if p[0] != "#"]
				code_list = preprocessor(code)
				try:
					k = self.interprete(code_list,{})
					print(k)
				except Exception as es:
					es = str(es).replace("Python","VHUK")
					self.answer_box.appendPlainText("ERROR:  " + str(es))

		except(FileNotFoundError):
			self.answer_box.appendPlainText("\nfile "+str(self.work_file_name.split("/")[-1])+" was deleted")








































	def debuger(self):
		self.answer_box.setPlainText("DEBUGING  0%")

		# f = open(self.work_file_name,"r")
		# g = f.read().splitlines()
		# f.close()
		g = self.textbox.toPlainText().splitlines()
		g.append("")
		length = len(g)
		for i in range(length):
			if g[i] == "":
				continue
			space_index = 0
			while g[i][-1] == " ":
				g[i] = g[i][:-1]
			while g[i][0] == " ":
				g[i] = g[i][1:]

			if "if" in g[i] or "for" in g[i] or "while" in g[i] or "else" in g[i] or "func" in g[i]:
				if g[i+1] == "":
					g[i+1] = "..."
				
				if g[i][-1] != "|":
					g[i] += "|"

				c = g[i+1].count("\t") - g[i].count("\t")
				if c > 1:
					g[i+1] = g[i+1][c-1:]
				elif c < 1:
					g[i+1] = "\t"*(2-(c+1)) + g[i+1]


			if "if" not in g[i] and "while" not in g[i]:
				if "<" in g[i] and "<<" not in g[i]:
					g[i] = g[i].replace("<","<<")
				if ">" in g[i] and ">>" not in g[i]:
					g[i] = g[i].replace(">",">>")

			line = "".join(g[i].split(" "))
			for j in debug_list_1:
				u = 30
				if j in "<>" and 'if' not in line and "while" not in line:
					continue
				if j == "=" or j == "==":
					u = 1
				line = line.replace(j," "+j+" ",u)
			for j in debug_list_2:
				line = line.replace(j,j+" ")
			g[i] = line



			self.answer_box.appendPlainText("DEBUGING  " + str(100*i/length) + "%")
		self.answer_box.appendPlainText("DEBUG COPLATE")

		text = "\n".join(g)
		self.textbox.setPlainText(text)











































app = QApplication(sys.argv)

inte = interpr()
inte.size_width = inte.frameGeometry().width()








# trayicon = QSystemTrayIcon(QIcon("IDE_settings/icon.png"),parent=app)
# trayicon.setToolTip("VHUK")
# trayicon.show()

# menu = QMenu()
# open_action = menu.addAction("open")
# open_action.triggered.connect(0)

# trayicon.setContextMenu(menu)


if __name__ == "__main__":
	inte.showMaximized()
	sys.exit(app.exec_())




#Zavaskoy funkcianery kanchel find_typeic