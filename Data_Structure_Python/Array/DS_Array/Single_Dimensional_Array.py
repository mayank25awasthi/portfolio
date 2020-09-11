class Array:
	def __init__(self,length,element=None,position=None):
		self.length=length
		self.arr_list=[]
		self.element=element
		self.position=position
		for i in range(length):
			self.arr_list.append(None)
		print(self.arr_list)
	def add_element(self,position,value):
		if len(self.arr_list)>position:
			self.arr_list[position]=value
			print(self.arr_list)
		else:
			print('Input Position greate than maximum length of an Array')

	def delete_element(self,value):
		if value in self.arr_list:
			for i,j in enumerate(self.arr_list):
				if j==value:
					self.arr_list[i]=None
		else:
			print('Specified value Dose not exists in array list')
			return
		print(self.arr_list)

	def update_element(self,value_1,value_2):
		if value_1 in self.arr_list:
			for i,j in enumerate(self.arr_list):
				if j==value_1:
					self.arr_list[i]=value_2
		else:
			print('Specified value Dose not exists in array list')
			return
		print(self.arr_list)

	def search_element(self,element):
		for i,j in enumerate(self.arr_list):
			if j==element:
				print(f'Element {element} is at {i} position in array list')
				break
		else:
			print(f'Element {element} is not present in array list')
