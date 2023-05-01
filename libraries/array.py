import ctypes as C
import sys
sys.path.append("..")


Lib = C.WinDLL("C:\\Users\\PC\\Desktop\\interp\\bin\\array_creator.dll")
Lib2 = C.WinDLL("C:\\Users\\PC\\Desktop\\interp\\bin\\array_math.dll")
Lib3 = C.WinDLL("C:\\Users\\PC\\Desktop\\interp\\bin\\res211.dll")



class Array():
	# def __init__(self,row=1,colum=1,minval=0,maxval=0,varient=0):
	def __init__(self, *args):
		if isinstance(args[0],list):
			self.make_array_with_list(args[0])
		elif isinstance(args[0],int) and isinstance(args[0],int):
			self.make_array_with_size(*args)



	def make_array_with_size(self,row,colum,minval=0,maxval=0,varient=0):
		self.row = row
		self.colum = colum
		if isinstance(minval,int):
			k = C.c_int * (self.row*self.colum)
			self.type = "int"
		elif isinstance(minval,float):
			k = C.c_double * (self.row*self.colum)
			self.type = "float"
		else:
			raise ValueError("Uncorrect varient value")
		self.arr = k()
		if isinstance(minval,int):
			Lib.make_int_array(self.arr,self.row,self.colum,minval,maxval,varient)
		elif isinstance(minval,float):
			Lib.make_double_array(self.arr,self.row,self.colum,C.c_double(minval),maxval,varient)

	def make_array_with_list(self,lst):
		self.row,self.colum = self.__right_list(lst)
		k = C.c_int * (self.row*self.colum) if isinstance(lst[0][0],int) else C.c_double * (self.row*self.colum)
		time_list = sum(lst,[])
		self.type = "int" if isinstance(time_list[0],int) else "float"
		self.arr = k(*time_list)

	def size(self):
		return [self.row,self.colum]

	def __str__(self):
		res = "\n"
		for i in range(0,self.row*self.colum,self.colum):
			for j in range(self.colum):
				res += str(self.arr[i+j]) + " "
			res += "\n"
		return res

	def __add__(self,other):
		if not isinstance(other,Array):
			return self.__number_operator(other,"+")
		else:
			row = min(self.row,other.row)
			colum = min(self.colum,other.colum)
			return self.__array_operator(other,row,colum,"entrywise_float_sum","entrywise_int_sum")

	def radd(self,other):
		row = min(self.row,other.row)
		colum = self.colum + other.colum
		return self.__array_operator(other,row,colum,"right_float_sum","right_int_sum")

	def badd(self,other):
		row = self.row + other.row
		colum = min(self.colum,other.colum)
		return self.__array_operator(other,row,colum,"bottom_float_sum","bottom_int_sum")

	def __neg__(self):
		time_array = Array(self.row,self.colum)
		for i in range(len(self.arr)):
			time_array.arr[i] = -self.arr[i]

		return time_array

	def __sub__(self,other):
		return self + (-other)


	def __pow__(self,other):
		if not isinstance(other,Array):
			return self.__number_operator(other,"**")
		else:
			row = self.row + other.row
			colum = self.colum + other.colum
			return self.__array_operator(other,row,colum,"direct_float_sum","direct_int_sum")

	def __mul__(self,other):
		if not isinstance(other,Array):
			return self.__number_operator(other,"*")
		else:
			row = self.row
			colum = other.colum
			return self.__array_operator(other,row,colum,"float_mul","int_mul")

	def entrywise_mul(self,other):
		if not isinstance(other,Array):
			raise TypeError("uncorrect type for entrywise mul")
		row = min(self.row,other.row)
		colum = min(self.colum,other.colum)
		return self.__array_operator(other,row,colum,"entrywise_float_mul","entrywise_int_mul")

	def __truediv__(self,other):
		return self * (other ** -1)


	def __getitem__(self,index):
		print(index)
		if isinstance(index,tuple):
			if len(index) != 2:
				raise ValueError("uncorrect arguments for slice")
			arg1,arg2 = index
			cond_int_1,cond_int_2 = isinstance(arg1,int),isinstance(arg2,int)
			cond_slice_1,cond_slice_2 = isinstance(arg1,slice),isinstance(arg2,slice)

			if not ((cond_int_1 or cond_slice_1) and (cond_int_2 or cond_slice_2)):
				raise TypeError("uncorrect type for slice")

			
			if cond_int_1 and cond_int_2:
				if arg2 >= self.colum or arg1 >= self.row:
					raise ValueError("index error")
				return self.arr[arg1 * self.colum + arg2]

			start_1,stop_1,step_1 = 0,self.row,1
			start_2,stop_2,step_2 = 0,self.colum,1

			if cond_slice_1 and cond_slice_2:
				start_1,stop_1,step_1 = self.__slice_info(arg1,self.row)
				start_2,stop_2,step_2 = self.__slice_info(arg2,self.colum)
			elif cond_slice_1 and cond_int_2:
				start_1,stop_1,step_1 = self.__slice_info(arg1,self.row)
				start_2,stop_2,step_2 = arg2,arg2+1,1
			elif cond_int_1 and cond_slice_2:
				start_1,stop_1,step_1 = arg1,arg1+1,1
				start_2,stop_2,step_2 = self.__slice_info(arg2,self.colum)

			# start_1 = self.__equalize(start_1,self.row,0,self.row)
			# start_2 = self.__equalize(start_2,self.row,0,self.row)

			# stop_1 = self.__equalize(stop_1,self.colum,0,self.colum+1)
			# stop_2 = self.__equalize(stop_2,self.colum,0,self.colum+1)

			print(start_1,stop_1,step_1)
			print(start_2,stop_2,step_2)

			if (stop_1 - start_1) * step_1 < 0 or (stop_2 - start_2) * step_2 < 0:
				raise ValueError("uncorrect values for slice")
			if step_1 == 0 or step_2 == 0:
				raise ValueError("uncorrect values for slice")

			rows = 0
			for _ in range(start_1,stop_1,step_1): rows += 1
			colums = 0
			for _ in range(start_2,stop_2,step_2): colums += 1

			time_array = Array(rows,colums,self.arr[0])
			eval("Lib3." + self.type + "_slice")(time_array.arr,self.arr,self.row,self.colum,
										start_1,stop_1,step_1,start_2,stop_2,step_2)
			return time_array


			
		elif isinstance(index,slice):
			start1,stop1,step1 = self.__slice_info(index,self.row)
			start2,stop2,step2 = 0,self.colum,1
			print(start1,stop1,step1)
		else:
			raise ValueError("uncorrect arguments for slice")


	def __slice_info(self,index,val):
		start = index.start if index.start else 0
		stop = index.stop if index.stop or index.stop == 0 else val
		step = index.step if index.step else 1
		if step < 0 and index.start == None and index.stop == None:
			start,stop = stop-1,start-1
		return start,stop,step


	def __setitem__(self,index,value):
		if not isinstance(value,(int,float)):
			raise TypeError("Array items must have type int or float")
		# value = eval(self.type)(value)
		self.arr[index[0]*self.colum + index[1]] = value


	def int(self):
		time_array = Array(self.row,self.colum,0)
		for i in range(self.row*self.colum):
			time_array.arr[i] = int(self.arr[i])
		return time_array

	def float(self):
		time_array = Array(self.row,self.colum,0.0)
		for i in range(self.row*self.colum):
			time_array.arr[i] = float(self.arr[i])
		return time_array



	def det(self):
		if self.row != self.colum:
			return None
		time_value = self.arr[0]
		if self.type == "int":
			Lib3.int_determinant(self.arr,self.row)
		elif self.type == "float":
			Lib3.float_determinant(self.arr,self.row)
		res = self.arr[0]
		self.arr[0] = time_value
		return res
	
	def inv(self):
		if self.row != self.colum:
			return None
		time_array = Array(self.row,self.colum,0.0)
		if self.type == "int":
			Lib3.int_inverse(time_array.arr,self.arr,self.row)
		elif self.type == "float":
			Lib3.float_inverse(time_array.arr,self.arr,self.row)
		return time_array

	def mirror(self,varient = 0):
		return self.__convertor(varient,"float_mirror","int_mirror")


	def transpose(self, varient = 0):
		return self.__convertor(varient,"float_transpose","int_transpose")
	

	def rotate(self, varient = 0):
		varient = self.__equalize(varient,4,0,4)
		if varient == 0:
			return self.rotate(1).rotate(3) 
		if varient == 1:
			return self.__convertor(0,"float_rotate","int_rotate")
		if varient == 2:
			return self.rotate(1).rotate(1)
		if varient == 3:
			return self.__convertor(15,"float_rotate","int_rotate")


	def gauss_transform(self):
		time_array = Array(self.row,self.colum,0.0)
		eval("Lib3." + self.type + "_gauss")(time_array.arr,self.arr,self.row,self.colum)
		return time_array




	def __equalize(self,val,padding,minval,maxval):
		while (cond := val < minval) or val >= maxval:
			val = val + padding if cond else val - padding
		return val


	def __convertor(self,varient,float_name,int_name):
		k = self.colum,self.row
		if "mirror" in int_name:
			k = self.row,self.colum
		if self.type == "int":
			time_array = Array(*k,0)
			eval("Lib3."+int_name)(time_array.arr,self.arr,self.row,self.colum,varient)
		else:
			time_array = Array(*k,0.0)
			eval("Lib3."+float_name)(time_array.arr,self.arr,self.row,self.colum,varient)
		return time_array

	def __number_operator(self,other,operator):
		if self.type == "float" or isinstance(other,float) or (other < 0 and operator == "**"):
			time_array = Array(self.row,self.colum,0.0)
			time_array.arr = (C.c_double * (self.row*self.colum))(*[self.__operate(i,operator,other) for i in self.arr])
		elif isinstance(other,int):
			time_array = Array(self.row,self.colum,0)
			time_array.arr = (C.c_int * (self.row*self.colum))(*[int(self.__operate(i,operator,other)) for i in self.arr])
		else:
			raise TypeError("uncorrect")
		return time_array


	def __array_operator(self,other,row,colum,float_name,int_name):
		cond_1 = self.type == "float"
		cond_2 = other.type == "float"

		if cond_1 or cond_2:
			time_array = Array(row,colum,0.0)
			if cond_1 and cond_2:
				eval("Lib2."+float_name)(time_array.arr,self.arr,other.arr,self.row,self.colum,other.row,other.colum)
			elif cond_1:
				other.change_type_to_float()
				eval("Lib2."+float_name)(time_array.arr,self.arr,other.arr,self.row,self.colum,other.row,other.colum)
				other.change_type_to_int()
			elif cond_2:
				self.change_type_to_float()
				eval("Lib2."+float_name)(time_array.arr,self.arr,other.arr,self.row,self.colum,other.row,other.colum)
				self.change_type_to_int()
		else:
			time_array = Array(row,colum,0)
			eval("Lib2."+int_name)(time_array.arr,self.arr,other.arr,self.row,self.colum,other.row,other.colum)

		return time_array


	def __right_list(self,lst):
		for i in lst:
			if not isinstance(i,list):
				raise Exception("Uncorrect list")
		lenght = len(lst[0])
		for i in lst:
			if len(i) != lenght:
				raise ValueError("Uncorrect list")

		cond = False
		for i in range(len(lst)):
			for j in range(len(lst[0])):
				if (cond := isinstance(lst[i][j],float)):
					break
			if cond:
				break

		if cond:
			for i in range(len(lst)):
				lst[i] = [float(j) for j in lst[i]]

		return len(lst),len(lst[0])



	def change_type_to_float(self):
		self.arr = (C.c_double * (self.row*self.colum))(*self.arr)

	def change_type_to_int(self):
		self.arr = (C.c_int * (self.row*self.colum))(*map(int,self.arr))

	def __operate(self,o1,e,o2):
		r = ["+","*","**"]
		if e not in r:
			return 0		
		if e == "+":
			return o1 + o2
		if e == "*":
			return  o1 * o2
		if e == "**":
			if o2 < 0:
				if o1 == 0 or o1 == 0.0:
					return float("inf")
				if o1 == -0.0:
					return float("-inf")
			return  (o1 ** o2)




# print(Array(4,4,3,3,varient="d"))
# # print(-Array([[1,2],[3,4]]))
# a = Array([[6,2,5],[3,0,9],[1,8,4]])



# print(a[::-1,::-1])

# # # a = Array(2,3,4)
# # b = Array([[20,4],[1,5]])
# # c = Array([[3]])
# k = Array(3,3,2)

# print(a.entrywise_mul(k))

# a = Array([[1, 2, 3],[4, 5, 6],[7,8,9]])

# print(a.transpose())

# print(a)
# # print(a.mirror(0))
# # print(a.mirror(1))


# print(a**3)
# print(a.det())
# print(a.transpose(1))
# print(k)
# print(k.inv())



# c = Array(2,2,1,varient=1)
# print(a)
# print(b)
# print(c) 
# print(b / c)
# print(a + 3)
# print(b)
# print(c)

# print(a.det())
# print(b.det())
# print(c.det())

# # print(a**b)
# # print(a+b)
# print(a)
# print(b)
# print(c)

