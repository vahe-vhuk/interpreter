from sys import path
path.append("../")

string_function_names = ["s_len", "s_slice", "s_concat", "to_str", "s_join", "s_lower",
						 "s_upper", "s_title", "s_count", "str_to_dict", "s_find", "s_split",
						 "s_rfind", "s_swapcase"]



def string_func(arif,variable_dict):
	from arifmetic.test import find_type,recurs_arifmetic
	func_name = arif.split("<<")[0].split("'")[-1]
	stri = arif.split("'")[0] if "'" in arif else None
	if stri != None:
		if not isinstance(variable_dict[stri],str) or stri not in variable_dict:
			raise ValueError(f"string with name {stri} not found")
	# args = arif.split("<<")[1].split(">>")[0].split(",")
	args = [recurs_arifmetic(k,variable_dict) for k in arif[arif.index("<<")+2:arif.rindex(">>")].split(",")]
	print(args,112121)
	if args == [""]:
		args = []



	#functin for counting len of string => s_len<<arg>>
	############################################################
	if func_name == "s_len":
		if len(args) != 1:
			raise ValueError("Function s_len<<>> must use one argument")
		arg = args[0]
		if arg[0] != "~":
			raise SyntaxError("Type string must begin with symbol ~")
		return len(arg)-1
	############################################################


	#Function for copying string with special indexes => s_cat<<arg1, *arg2, *arg3>>
	############################################################
	elif func_name == "s_slice":
		if not 0 <= len(args) <= 3:
			raise ValueError("Function copy<<>> must use one, two or three arguments")
		if len(args) == 0:
			return variable_dict[stri][:]
		if len(args) == 1:
			index = find_type(args[0])
			return "~" + variable_dict[stri][index+1]
		if len(args) == 2:
			start,stop = find_type(args[0]),find_type(args[1])
			if start == "" or start == " ":
				start = 0
			if stop == "" or stop == " ":
				stop = len(variable_dict[stri])
			return "~" + variable_dict[stri][start+1:stop+1]
		if len(args) == 3:
			start,stop,step = find_type(args[0]),find_type(args[1]),find_type(args[2])
			if start == "" or start == " ":
				start = 0 if step > 0 else len(variable_dict[stri])
			if stop == "" or stop == " ":
				stop = 0 if step < 0 else len(variable_dict[stri]) 
			return "~" + variable_dict[stri][start+1:stop+1:step]

	############################################################


	#function for concating strings => s_concat<<arg1, arg2, *arg3, ...>>
	############################################################
	elif func_name == "s_concat":
		if len(args) < 2:
			raise ValueError("Function s_concat<<>> must use two or more arguments")
		res = "~"
		for arg in args:
			if not isinstance(arg,str):
				raise TypeError("Function s_concat mustn't use with this type")
			if arg[0] != "~":
				raise SyntaxError("Type string must begin with symbol ~")
			res += arg[1:]
		return res
	############################################################


	#Function for convert numbers to string => to_str<<arg1>>
	############################################################
	elif func_name == "to_str":
		if len(args) != 1:
			raise ValueError("Function to_str<<>> must use one argument")
		return "~" + str(args[0])
	############################################################


	#Function for convert list to string with special tabs => s_join<<arg1, *arg2>>
	############################################################
	elif func_name == "s_join":
		if len(args) != 1:
			raise ValueError("Function s_join<<>> must use one argument")
		arg = args[0]
		if not isinstance(arg,list):
			raise TypeError("argument in s_join<<>> must have type list")
		arg = [str(s) for s in arg]
		val = variable_dict[stri] if stri else " "
		return "~" + val.join(arg)
	############################################################


	#function lower => s_lower<<>>
	############################################################
	elif func_name == "s_lower":
		if len(args) != 0:
			raise ValueError("Function s_lower<<>> mustn't use eny arguments")
		return "~" + variable_dict[stri][1:].lower()
	############################################################


	#function upper => s_upper<<>>
	############################################################
	elif func_name == "s_upper":
		if len(args) != 0:
			raise ValueError("Function s_upper<<>> mustn't use eny arguments")
		return "~" + variable_dict[stri][1:].upper()
	############################################################


	#function title => s_title<<>>
	############################################################
	elif func_name == "s_title":
		if len(args) != 0:
			raise ValueError("Function s_title<<>> mustn't use eny arguments")
		return "~" + variable_dict[stri][1:].title()
	############################################################


	#Function for counting special symbol in string => s_count<<arg1, *arg2>>
	############################################################
	elif func_name == "s_count":
		if not 0 <= len(args) <= 1:
			raise ValueError("Functin s_count<<>> must use zero or one argument")
		arg = args[0] if len(args) == 1 else "~ "
		if not isinstance(arg,str):
			raise TypeError("Firs argument in c_count<<>> must have type string")
		if arg[0] != "~":
			raise SyntaxError("Type string must begin with symbol ~")
		return variable_dict[stri].count(arg[1:])
	############################################################
