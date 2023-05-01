from sys import path
path.append("../")

list_function_names = ["list","append","pop","index","len","addlist","clear", "set",
					   "count","insert","reverse","sort","slice","list_info","l_swap", "to_list"]

def list_func(arif,variable_dict):
	from arifmetic.test import find_type,recurs_arifmetic
	func_name = arif.split("<<")[0].split("'")[-1]
	lst = arif.split("'")[0] if "'" in arif else None
	if lst != None:
		if not isinstance(variable_dict[lst],list) or lst not in variable_dict:
			raise ValueError(f"list with name {lst} not found")
	# args = arif.split("<<")[1].split(">>")[0].split(",")
	klo = sl(arif[arif.index("<<")+2:arif.rindex(">>")])
	args = [find_type(k,variable_dict) for k in klo]
	if args == [""]:
		args = []


	#List maker function => list<<*arg1, *arg2, ...>>
	############################################################
	if func_name == "list":
		ls = []
		for arg in args:
			arg = recurs_arifmetic(arg,variable_dict)
			ls.append(arg)
		return ls
	############################################################

	#List lenght counter function => len<<arg1>>
	############################################################
	elif func_name == "len":
		if len(args) != 1:
			raise ValueError("Function len<<>> must use one argument")
		arg = args[0]
		# if arg not in variable_dict:
		# 	raise ValueError(f"List with name {arg} not found")
		if not isinstance(arg,list):
			raise TypeError("The len<<>> function mustn't be used with the this type")
		return len(arg)
	############################################################

	#Function for pop element with list => pop<<arg1, *arg2>>
	############################################################
	elif func_name == "pop":
		if not 0 <= len(args) <= 1:
			raise ValueError("Function pop<<>> must use zero or one arguments")
		if not isinstance(variable_dict[lst],list) or lst not in variable_dict:
			raise ValueError(f"list with name {lst} not found")
		if len(args) == 0:
			arg = len(variable_dict[lst]) - 1
		else:
			arg = recurs_arifmetic(args[0],variable_dict)
		if not isinstance(arg,int):
			raise TypeError("Function pop<<>> must use type int")
		return variable_dict[lst].pop(arg)
	############################################################



	#Function for appending elemend in the list => append<<arg1, *arg2, ...>>
	############################################################
	elif func_name == "append":
		if len(args) < 1:
			raise ValueError("Function append<<>> must use one or more arguments")
		if not isinstance(variable_dict[lst],list) or lst not in variable_dict:
			raise TypeError("Function append<<>> must be work for the lists")
		for arg in args:
			arg = recurs_arifmetic(arg,variable_dict)
			variable_dict[lst].append(arg)
		return None
	############################################################


	#Function for appending elemend by the index in the list => insert<<arg1, arg2>>
	############################################################
	elif func_name == "insert":
		if len(args) != 2:
			raise ValueError("Function insert<<>> must use two arguments")
		arg1 = find_type(args[0])
		arg2 = find_type(args[1])
		print(arg1,type(arg1))
		print(arg2,type(arg2))
		if not isinstance(arg2,int):
			raise ValueError("In second argument in insert<<>> must be used type int")
		variable_dict[lst].insert(arg2,arg1)
	############################################################



	#Function for return index of element with list => index<<arg1, arg2>>
	############################################################
	elif func_name == "index":
		if len(args) != 1:
			raise ValueError("Function index<<>> must use one argument")
		arg = recurs_arifmetic(args[0],variable_dict)
		try:
			return variable_dict[lst].index(arg)
		except(ValueError):
			return -1
	############################################################


	#Function for add up few lists => addlist<<arg1, arg2, *arg3, ...>>
	############################################################
	elif func_name == "addlist":
		if len(args) < 1:
			raise ValueError("Function addlist<<>> must use one or more arguments")
		if lst not in variable_dict or not isinstance(variable_dict[lst],list):
			raise TypeError("not list")
		
		for arg in args:
			if not isinstance(variable_dict[arg],list):
				raise TypeError("Function addlist<<>> mustn't be used arguments with this type")
			variable_dict[lst] += variable_dict[arg]
		return None
	############################################################


	#Function for clear list => clear<<>>
	############################################################
	elif func_name == "clear":
		if len(args) != 0:
			raise ValueError("Function clear<<>> mustn't use eny arguments")
		variable_dict[lst].clear()
		return None
	############################################################


	############################################################
	elif func_name == "count":
		if len(args) != 1:
			raise ValueError("Function count<<>> must use one argument")
		arg = recurs_arifmetic(args[0],variable_dict)
		return variable_dict[lst].count(arg)
		
	############################################################


	#Function for reverse list => reverse<<>>
	############################################################
	elif func_name == "reverse":
		if len(args) != 0:
			raise ValueError("Function reverse<<>> mustn't use eny arguments")
		variable_dict[lst].reverse()
		return None
	############################################################


	#Function for sort list => sort<<>>
	############################################################
	elif func_name == "sort":
		if len(args) != 0:
			raise ValueError("Function sort<<>> mustn't use eny arguments")
		variable_dict[lst].sort()
		return None
	############################################################


	#Function for copy piece of the list => copy<<arg1, *arg2, *arg3, *arg4>>
	############################################################
	elif func_name == "slice":
		if not 0 <= len(args) <= 3:
			raise ValueError("Function copy<<>> must use one, two or three arguments")
		if len(args) == 0:
			return variable_dict[lst][:]
		if len(args) == 1:
			index = find_type(args[0])
			return variable_dict[lst][index]
		if len(args) == 2:
			start,stop = find_type(args[0]),find_type(args[1])
			if start == "" or start == " ":
				start = 0
			if stop == "" or stop == " ":
				stop = len(variable_dict[lst])
			return variable_dict[lst][start:stop]
		if len(args) == 3:
			start,stop,step = find_type(args[0]),find_type(args[1]),find_type(args[2])
			if start == "" or start == " ":
				start = 0 if step > 0 else len(variable_dict[lst])
			if stop == "" or stop == " ":
				stop = 0 if step < 0 else len(variable_dict[lst]) 
			return variable_dict[lst][start:stop:step]

	############################################################


	#Function for swaping elements with list => l_swap<<arg1, arg2>>
	############################################################
	elif func_name == "l_swap":
		if len(args) != 2:
			raise ValueError("Function count<<>> must use two arguments")
		arg1 = recurs_arifmetic(args[0],variable_dict)
		arg2 = recurs_arifmetic(args[1],variable_dict)
		if not isinstance(arg1,int) or not isinstance(arg2,int):
			raise TypeError("List indexes must have type int")
		variable_dict[lst][arg1],variable_dict[lst][arg2] = variable_dict[lst][arg2],variable_dict[lst][arg1]
		return None
	############################################################



	#Function for set element in index => set<<arg1,arg2>>
	############################################################
	elif func_name == "set":
		if len(args) != 2:
			raise ValueError("Function set<<>> must use two arguments")
		arg1 = recurs_arifmetic(args[0],variable_dict)
		arg2 = recurs_arifmetic(args[1],variable_dict)
		if not isinstance(arg1,int):
			raise TypeError("list index must have type int")
		variable_dict[lst][arg1] = arg2
		return None

	############################################################


	#Function for convert sting to list => to_list<<arg1>>
	############################################################
	elif func_name == "to_list":
		if len(args) != 1:
			raise ValueError("Function to_list<<>> must use one argument")
		arg = recurs_arifmetic(args[0],variable_dict)
		arg = str(arg)
		if arg[0] == "~":
			arg = arg[1:]
		return list(arg)
	############################################################



	#Function for printing info about lists => list_info<<>>
	############################################################
	elif func_name == "list_info":
		if len(args) != 0:
			raise ValueError("Function sort<<>> mustn't use eny arguments")
		info = """
		There are 15 function for working with lists
		"list", "append", "pop", "index", "len", "addlist", "to_list"
		"clear","count","insert","reverse","sort","copy" and "list_info"


		'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


		Functions "list", "addlidt", "to_list" and "copy" are meke new lists


		Functions "append", "clear", "insert", "reverse", "l_swap", "set", "pop" and "sort"
				  are make changes into lists

		Functions "pop", "index", "len" and "count" are accept list with 
				  argument and returns adequate values

		Function  "list_info" returns information about the list functions

		'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


		val:list = list<<*arg1:eny_type, *arg2:eny_type, ...>>

				   This function creats a list on the bases of
				   the given arguments
				   Equivalent in python

				    val = list(arg1,arg2,...)

		val:list = addlist<<*arg1:eny_type, *arg2:eny_type, ...>>

				   This function concatinates the lists
				   Equivalent in python

				    val = arg1 + arg2

		val:list = copy<<arg1:list, *arg2:int, *arg3:int, *arg4:int>>

				   This function copies the list into other list 
				   acording to special indexes
				   Equivalent in python
 
				    val = copy<<arg1>>   ==>>  list_2 = copy(list_1)
				    val = copy<<arg1, arg2>>   ==>>  list_2 = list_1[arg2]
				    val = copy<<arg1, arg2, arg3>>   ==>>  list_2 = list_1[arg2:arg3]
				    val = copy<<arg1, arg2, arg3, arg4>>   ==>>  list_2 = list1[arg2:arg3:arg4]


		val:some_list = append<<arg1:eny_type, *arg2:eny_type, arg3:eny_type, ...>>

				   This function appends values (arg1, arg2, ...) into the list val
				   Equivalent in python

				    list.append(arg)

		val:some_list = clear<<>>

				   This function clears the list val
				   Equivalent in python

				    list.clear()

		val:some_list = l_swap<<arg1, arg2>>

				   This function swaps elements in the list from indexes arg1, arg2
				   Equivalent in python

				    NOT

		val:some_list = set<<arg1, arg2>>

				   This function sets value arg1 of the element in the list with index arg2
				   Equivalent in python

				    NOT

		val:some_list = insert<<arg1:eny_type, arg2:int>>

				   This function inserts element arg1 includes the list val in index arg2
				   Equivalent in python

				    list.insert(arg2, arg1)

		val:some_list = reverse<<>>

				   This function reverses the list val
				   Equivalent in python

				    list.reverse()

		val:some_list = sort<<>>

				   This function sorts the list val
				   Equivalent in python

				    list.sort()

		val:int = pop<<arg1:list, *arg2:int>>

				   This function pops and returns element from index arg2 or last element
				   Equivalent in python

				    val = list.pop(arg2)

		val:int = index<<arg1:list, arg2:eny_type>>

				   This function returns the index of element arg2 from list arg1
				   Equivalent in python

				    val = list.index(arg2)

		val:int = len<<arg1:list>>

				   This function returns the lenght of list arg1
				   Equivalent in python

				    val = len(arg1)

		val:int = count<<arg1:list, arg2:eny_type>>

				   This function counts and returns the amount of elements arg2 from list arg1
				   Equivalent in python

				    val = list.count(arg2)

		val:list = to_list<<arg1:eny_type>>

				   This function makes list with simvols of arg1
				   Equivalent in python

				    None

		val:string = list_info<<>>

				   This function returns information about the list functions
			   """
		return info
	############################################################

def sl(a):
	l = []
	k = ""
	for i in a:
		if i == "," and len(l) == 0:
			k += "!"
		else:
			if i == "<":
				l.append(i)
			elif i == ">":
				l.pop()
			k+= i
	return k.split("!")