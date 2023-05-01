from time import sleep
from sys import path
path.append("../")
from intergatet_functions.lists import list_function_names,list_func
from intergatet_functions.dicts import dict_func,dict_function_names
from intergatet_functions.strings import string_func,string_function_names
from intergatet_functions.arrays import array_func,array_function_names
from libraries.array import Array


functions_dict = {}
functions_argumens_dict = {}

def find_type(a,variable_dict = {}):
	f = ["0","1","2","3","4","5","6","7","8","9",".","-"," "]
	if not isinstance(a,str):
		return a
	if a == "":
		return ""
	if a == "pi":
		return 3.141592653589
	if a in variable_dict:
		return variable_dict[a]
	try:
		a = int(a)
	except Exception:
		try:
			a = float(a)
		except Exception:
			pass


		######################################################difined functions
		if isinstance(a,str):
			func_name = a.split("<<")[0]
			if func_name in functions_dict:
				l = a.split("<<")[1].split(">>")[0].split(",")
				if len(l) == len(functions_dict[func_name][0]):
					values = functions_dict[func_name][0]
					for z in range(len(l)):
						l[z] = recurs_arifmetic(l[z],variable_dict)###################################
					res = {}
					for key in values:
					    for value in l:
					        res[key] = value
					        l.remove(value)
					        break 
					functions_argumens_dict[func_name] = res
				else:
					raise TypeError("Uncorrect arguments count")


			elif func_name.split("'")[-1] in list_function_names:
				return list_func(a,variable_dict)
			elif func_name.split("'")[-1] in dict_function_names:
				return dict_func(a,variable_dict)
			elif func_name.split("'")[-1] in string_function_names:
				return string_func(a,variable_dict)
			elif func_name.split("'")[-1] in array_function_names:
				return array_func(a,variable_dict)

	return a





def find_index(value,a1,a2):
	i1,i2 = -1,-1
	for i in range(len(value)):
		if value[i] == a1:
			i1 = i
		if value[i] == a2:
			i2 = i
			break
	return i1,i2


def klo(a):
	l = []
	d = {"[":"]","{":"}","(":")"}
	for i in a:
		if i in "([{":
			l.append(i)
		if i in ")]}":
			if len(l) == 0:
				return False
			k = l.pop()
			if i != d[k]:
				return False
	if len(l) == 0:
		return True
	return False





def operate(o1,e,o2,variable_dict):
	r = ["+","-","*","/","%","//","^"]
	if e not in r:
		return 0		
	o1 = find_type(o1,variable_dict)
	o2 = find_type(o2,variable_dict)
	
	if e == "+":
		if isinstance(o1,str) and isinstance(o2,str):
			return o1 + o2[1:]
		return o1 + o2
	if e == "-":
		return  o1 - o2
	if e == "%":
		return  o1 % o2
	if e == "*":
		return  o1 * o2
	if e == "/":
		res = o1 / o2
		return int(res) if res == int(res) else res
	if e == "//":
		return  o1 // o2
	if e == "^":
		return  (o1 ** o2)



def recurs_arifmetic(a,variable_dict):
	# if a[0] == "~":
	# 	return a
	# if ":" in a:
	# 	return a
	if not isinstance(a,str):
		return a
	res = find_type(a,variable_dict)
	if not isinstance(res,str):
		return res



	a = str(a)

	c = klo(a)
	if not c:
		raise SyntaxError("Uncorrect arefmetic")

	# if ":" in a:
	# 	time_dict = {}
	# 	for i in a.split(" "):
	# 		w = i.split(":")
	# 		time_key = find_type(w[0],variable_dict)
	# 		time_value = find_type(w[1],variable_dict)
	# 		if isinstance(time_value,Array):
	# 			time_value = str(time_value)
	# 		time_dict[time_key] = time_value
	# 	return time_dict
	if ";" in a:
		return [recurs_arifmetic(k,variable_dict) for k in a.split(";")]


	t = "".join([f for f in  a.split(" ") if f != ""])
	operator_count = 0
	for i in ['+','*',"^",'/','//','%',"-","(",")"]:
		if i in t:
			operator_count += 1
		t = t.replace(i," "+i+" ",30)
	if operator_count != 0:
		t = [k for k in t.split(" ") if k != ""]
	else:
		t = [find_type(k,variable_dict) for k in a.split(" ") if k != ""]




	while "(" in t or ")" in  t:
		i1,i2 = find_index(t,"(",")")
		t[i1:i2+1] = [arifmetic(t[i1+1:i2],variable_dict)]

	return arifmetic(t,variable_dict)





def arifmetic(t,variable_dict):
	print(t)
	if len(t) == 2:
		res = find_type(t[1],variable_dict)
		if t[0] == "-" and isinstance(res,(int,float,Array)):
			return -res
		# raise SyntaxError("Uncorrect arithmetic expression")


	for i in ["-",'^','*',"/",'//','%','+']:
		while i in t:
			ind = t.index(i)
			if i =="-":
				g = -find_type(t[ind+1],variable_dict)
				if ind == 0 or t[ind-1] in ["-",'^','*',"/",'//','%','+']:
					t[ind:ind+2] = [g]
				else:
					t[ind:ind+2] = ["+",g]
			elif i == "/" and (t[ind-1] == i or t[ind+1] == i):
				if t[ind-1] == i:
					t[ind-1:ind+1] = ["//"]
				elif t[ind+1] == i:
					t[ind:ind+2] = ["//"]
			else:
				g = operate(t[ind - 1],i,t[ind + 1], variable_dict)
				t[ind-1:ind+2] = [g]

	if len(t) == 1:
		return find_type(t[0],variable_dict)
	return t

	if a[0] == " ":
		a = a[1:]
	if a[0] != "~":
		raise SyntaxError("Type string must begin with symbol ~")
	return a










