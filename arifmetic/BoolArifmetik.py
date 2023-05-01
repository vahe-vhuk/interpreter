from sys import path
path.append("../")
from arifmetic.test import recurs_arifmetic,find_index

def find_value(a):
	if a:
		return True
	else:
		return False


def bool_operate(o1,e,o2, variable_dict):
	if e not in [">","<","==",">=","<=","!=","&&","||"]:
		return 0
	o1 = recurs_arifmetic(o1, variable_dict)
	o2 = recurs_arifmetic(o2, variable_dict)
	if e == ">":
		return  o1 > o2
	if e == "<":
		return  o1 < o2
	if e == "<=":
		return  o1 <= o2
	if e == ">=":
		return  o1 >= o2
	if e == "==":
		return  o1 == o2
	if e == "!=":
		return  o1 != o2
	if e == "&&":
		if o1 == "True" and o2 == "True":
			return True
		if o1 == "False" and o2 == "True":
			return False
		if o1 == "True" and o2 == "False":
			return False
		if o1 == "False" and o2 == "False":
			return False
	if e == "||":
		# if o1 == "True" and o2 == "True":
		# 	return True
		# if o1 == "False" and o2 == "True":
		# 	return True
		# if o1 == "True" and o2 == "False":
		# 	return True
		# if o1 == "False" and o2 == "False":
			return eval(o1) or eval(o2)				


def recurs_bool_arifmetic(a,variable_dict):
	i1 = find_index(a,"(",")")[0]
	i2 = find_index(a,"(",")")[1]


	if a == "" or a == 0 or a == " ":
		return False
	if i1 == -1 and i2 == -1:
		return bool_arifmetic(a, variable_dict)		
	if i1 != -1 and i2 != -1 and i1 < i2:
		return recurs_bool_arifmetic(a[:i1] + str(recurs_bool_arifmetic(a[i1+1:i2],variable_dict)) + a[i2+1:],variable_dict)


def bool_arifmetic(a,variable_dict):
	t = a.split(" ")
	if len(t) == 1 :
		return find_value(a)
	if len(t) == 2:
		if t[0] == "!":
			return not find_value(a)
		return False		
	if t[1] in [">","<","==",">=","<=","!=","&&","||"]:
		return bool_operate(t[0],t[1],t[2],variable_dict)


