from sys import path
path.append("../")


dict_function_names = ["dict","d_set","d_pop","d_clear","dict_info",
					   "d_swap","d_keys","d_values","d_get"]


def find_value(arg,variable_dict):
	from arifmetic.test import find_type,recurs_arifmetic
	arg1,arg2 = arg.split(":")
	arg1 = recurs_arifmetic(arg1,variable_dict)
	arg2 = recurs_arifmetic(arg2,variable_dict)
	return arg1,arg2



def dict_func(arif,variable_dict):
	from arifmetic.test import find_type,recurs_arifmetic
	func_name = arif.split("<<")[0].split("'")[-1]
	dct = arif.split("'")[0] if "'" in arif else None
	# args = arif.split("<<")[1].split(">>")[0].split(",")
	args = [k for k in arif[arif.index("<<")+2:arif.rindex(">>")].split(",")]
	# print(args,12313131)
	if args == [""]:
		args = []


	#Function for creat dict => dict<<*arg1:value1, *arg2:value2, ...>>
	############################################################
	if func_name == "dict":
		diction = {}
		for arg in args:
			if not ":" in arg:
				raise ValueError("Uncorrect argument value")
			arg1,arg2 = find_value(arg,variable_dict)
			if not isinstance(arg1,(str,int,tuple)):
				raise TypeError("Dict keys must be hashable")
			diction[arg1] = arg2
		return diction
	############################################################

	#Function for add elements in dict => d_set<<arg1:value1, *arg2:value2, ...>>
	############################################################
	elif func_name == "d_set":
		if len(args) < 1:
			raise ValueError("Function d_set<<>> must use one or more arguments")
		if not isinstance(variable_dict[dct],dict) or dct not in variable_dict:
			raise ValueError(f"Dict with name {dct} not found")
		for arg in args:
			if not ":" in arg:
				raise ValueError("Uncorrect argument value")
			arg1,arg2 = find_value(arg,variable_dict)
			if not isinstance(arg1,(list,dict)):
				raise TypeError("Dict keys must be hashable")
			variable_dict[dct][arg1] = arg2
		return None
	############################################################


	#Function for pop and return element by key => d_pop<<arg1, arg2>>
	############################################################
	elif func_name == "d_pop":
		if len(args) != 1:
			raise ValueError("Function d_pop<<>> must use one argument")
		arg = recurs_arifmetic(args[0],variable_dict)
		if not isinstance(variable_dict[dct],dict) or dct not in variable_dict:
			raise ValueError(f"Dict with name {dct} not found")
		return variable_dict[dct].pop(arg)
	############################################################


	#Function for clering dict => d_clear<<>>
	############################################################
	elif func_name == "d_clear":
		if len(args) != 0:
			raise ValueError("Function d_clear<<>> mustn't use eny arguments")
		if not isinstance(variable_dict[dct],dict) or dct not in variable_dict:
			raise ValueError(f"Dict with name {dct} not found")
		variable_dict[dct].clear()
		return None
	############################################################


	#Function for swap values wit special keys => d_swap<<arg1,arg2>>
	############################################################
	elif func_name == "d_swap":
		if len(args) != 2:
			raise ValueError("Function d_swap<<>> must use two arguments")
		if not isinstance(variable_dict[dct],dict) or dct not in variable_dict:
			raise ValueError(f"Dict with name {dct} not found")
		arg1 = recurs_arifmetic(args[0],variable_dict)
		arg2 = recurs_arifmetic(args[1],variable_dict)
		variable_dict[dct][arg1],variable_dict[dct][arg2] = variable_dict[dct][arg2],variable_dict[dct][arg1]
		return None
	############################################################


	#Function for return dict keys list => d_keys<<arg1>>
	############################################################
	elif func_name == "d_keys":
		if len(args) != 0:
			raise ValueError("Function d_keys<<>> mustn't use any argument")
		if not isinstance(variable_dict[dct],dict) or dct not in variable_dict:
			raise ValueError(f"Dict with name {dct} not found")
		return list(variable_dict[dct].keys())
	############################################################


	#Function for return dict values list => d_values<<arg1>>
	############################################################
	elif func_name == "d_values":
		if len(args) != 0:
			raise ValueError("Function d_values<<>> mustn't use any arguments")
		if not isinstance(variable_dict[dct],dict) or dct not in variable_dict:
			raise ValueError(f"Dict with name {dct} not found")
		return list(variable_dict[dct].values())
	############################################################


	#Function for return value by key => d_get<<arg1, arg2>>
	############################################################
	elif func_name == "d_get":
		if len(args) != 1:
			raise ValueError("Function d_get<<>> must use two arguments")
		if not isinstance(variable_dict[dct],dict) or dct not in variable_dict:
			raise ValueError(f"Dict with name {dct} not found")
		arg = recurs_arifmetic(args[0],variable_dict)
		return variable_dict[dct][arg]
	############################################################

	# ############################################################
	# elif func_name == "dict_info":
	# 	if len(args) != 0:
	# 		raise ValueError("Function sort<<>> mustn't use eny arguments")
	# 	info = """
	# 	There are 9 function for working with dicts
	# 	    "dict","d_set","d_pop","d_clear",
	# 	    "dict_info","d_swap","d_keys","d_values","d_get"


	# 	'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


	# 	Function  "dict" mekes new lists


	# 	Functions "d_set", "d_pop", "d_clear", "d_swap"
	# 			  are make changes into dicts

	# 	Functions "d_pop", "d_keys", "d_values" and "d_get" are accept dict with 
	# 			  argument and returns adequate values

	# 	Function  "dict_info" returns information about the dict functions

	# 	'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


	# 	val:dict = dict<<*arg1:value1:eny_type, *arg2:value2:eny_type, ...>>

	# 			   This function creats a dict on the bases of
	# 			   the given arguments
	# 			   Equivalent in python

	# 			    val = dict(arg1 = value1, arg2 = value2, ...)

	# 	val:some_dict = d_set<<arg1:eny_type, arg2:eny_type>>

	# 			   This function adds arg2 in dict with key arg1
	# 			   Equivalent in python

	# 			    val[arg1] = arg2

	# 	val:same_dict = d_clear<<>>

	# 			   This function clears dict val
	# 			   Equivalent in python

	# 			    val.clear()

	# 	val:some_dict = d_swap<<arg1:eny_type, arg2:eny_type>>

	# 			   This function swaps elements in dict val from keys arg1 and arg2
	# 			   Equivalent in python

	# 			    val[arg1],val[arg2] = val[arg2],val[arg1]

	# 	val:eny_type = d_pop<<arg1:dict, arg2:eny_type>>

	# 			   This function returns and delets from dict arg1 value wit key arg2
	# 			   Equivalent in python

	# 			    val = arg1.pop(arg2)

	# 	val:list = d_keys<<arg1:dict>>

	# 			   This function returns list with keys arg1
	# 			   Equivalent in python

	# 			    val = list(arg1.keys())

	# 	val:list = d_values<<arg1:dict>>

	# 			   This function returns list with values arg1
	# 			   Equivalent in python

	# 			    val = list(arg1.values()) 

	# 	val:eny_type = d_get<<arg1:dict, arg2:eny_type>>

	# 			   This function returns value with key arg2 from dict arg1
	# 			   Equivalent in python

	# 			    val = arg1[arg2]

	# 	val:string = dict_info<<>>

	# 			   This function returns information about the dict functions
	# 		   """
	# 	variable_dict[t[0]] = info
	# ############################################################
