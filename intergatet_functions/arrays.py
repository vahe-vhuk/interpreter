from sys import path
path.append("../")
from libraries.array import Array


array_type_list = ["","d","t","td","b","bd","D","T","TD","B","BD"]
array_function_names = ["size","det","badd","radd","rotate",
						"transpose","mirror","gauss","inv","to_int","to_float",
						"entrywise_mul","setitem","getitem",
						"array"]+[i+"_array" for i in array_type_list]



def array_func(arif,variable_dict):
	print(arif,88888888888888888888)
	from arifmetic.test import find_type,recurs_arifmetic
	func_name = arif.split("<<")[0].split("'")[-1]
	arr = arif.split("'")[0] if "'" in arif else None
	if arr != None:
		if not isinstance(variable_dict[arr],Array) or arr not in variable_dict:
			raise ValueError(f"Array with name {arr} not found")
	# args = arif.split("<<")[1].split(">>")[0].split(",")
	args = [recurs_arifmetic(k,variable_dict) for k in arif[arif.index("<<")+2:arif.rindex(">>")].split(",")]
	print(args,112121)
	if args == [""] or args == [[]]:
		args = []



	if func_name == "array":
		if not 1 <= len(args) <= 3:
			raise ValueError("dwbsdjcwjhca")
		if len(args) == 1 and not isinstance(args[0],list):
			raise TypeError("jbh")
		if len(args) == 2 and not isinstance(args[0],int) and not isinstance(args[1],int):
			raise TypeError("dbjma")
		if len(args) == 3 and not isinstance(args[2],(int,float)):
			raise TypeError("few")
		return Array(*args)

	elif func_name[-5:] == "array" and (array_type := func_name.split("_")[0]) in array_type_list:
		if len(args) != 3 and not isinstance(args[3],(int,float)):
			raise ValueError("dwbsdjcwjhca")
		return Array(*args,varient=array_type_list.index(array_type))



	elif func_name == "size":
		if len(args) != 0:
			raise ValueError("fcwdwcwascsa")
		return variable_dict[arr].size()


	elif func_name == "det":
		if len(args) != 0:
			raise ValueError("cwcwcwe")
		return variable_dict[arr].det()

	elif func_name == "badd":
		if len(args) != 1:
			raise ValueError("cewcwc")
		print(args)
		if not isinstance(args[0],Array):
			raise TypeError("fwvwev")
		return variable_dict[arr].badd(args[0])

	elif func_name == "radd":
		if len(args) != 1:
			raise ValueError("ferve")
		if not isinstance(args[0],Array):
			raise TypeError("fwevebvae")
		return variable_dict[arr].radd(args[0])

	elif func_name == "entrywise_mul":
		if len(args) != 1:
			raise ValueError("ferve")
		if not isinstance(args[0],Array):
			raise TypeError("fwevebvae")
		return variable_dict[arr].entrywise_mul(args[0])

	elif func_name == "rotate":
		if len(args) != 1:
			raise ValueError("ferve")
		if not isinstance(args[0],int):
			raise TypeError("fwevebvae")
		return variable_dict[arr].rotate(args[0])


	elif func_name == "transpose":
		if len(args) != 1:
			raise ValueError("ferve")
		if not isinstance(args[0],int):
			raise TypeError("fwevebvae")
		return variable_dict[arr].transpose(args[0])

	elif func_name == "mirror":
		if len(args) != 1:
			raise ValueError("ferve")
		if not isinstance(args[0],int):
			raise TypeError("fwevebvae")
		return variable_dict[arr].mirror(args[0])


	elif func_name == "gauss":
		if len(args) != 0:
			raise ValueError("ferve")
		return variable_dict[arr].gauss_transform()

	elif func_name == "inv":
		if len(args) != 0:
			raise ValueError("ferve")
		return variable_dict[arr].inv()

	elif func_name == "to_int":
		if len(args) != 0:
			raise ValueError("ferve")
		return variable_dict[arr].int()

	elif func_name == "to_float":
		if len(args) != 0:
			raise ValueError("ferve")
		return variable_dict[arr].float()

	elif func_name == "setitem":
		if len(args) != 3:
			raise ValueError("fewcw")
		if not isinstance(args[0],int) or not isinstance(args[1],int):
			raise TypeError("fwewcwcwe")
		variable_dict[arr][args[0],args[1]] = eval(variable_dict[arr].type)(args[2])
		return None


	elif func_name == "getitem":
		if len(args) != 2:
			raise ValueError("fwvebvadveav")
		if isinstance(args[0],list):
			# if args[0][1] > variable_dict[arr].row or args[0][0] < 0:
			# 	raise ValueError("index error")
			args[0] = slice(*args[0])
		if isinstance(args[1],list):
			# if args[1][1] > variable_dict[arr].colum or args[1][0] < 0:
			# 	raise ValueError("index error")
			args[1] = slice(*args[1])
		return variable_dict[arr][args[0],args[1]]