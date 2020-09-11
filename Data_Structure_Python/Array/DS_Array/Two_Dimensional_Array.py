class Array2D:
	def __init__(self,rows,columns):
		self.rows=rows
		self.columns=columns
		self.arr_list=[]
		for i in range(self.rows):
			self.row_list=[]
			for j in range(self.columns):
				self.row_list.append(None)				
			self.arr_list.append(self.row_list)
		self.return_array()
	def return_array(self):
		for i in self.arr_list:
			for j in i:
				print(j,end ='  ')
			print()
						
	def add_element(self,pos1,pos2,value):
		if len(self.arr_list)>pos1:
			if len(self.arr_list[pos1])>pos2:
				self.arr_list[pos1][pos2]=value
				self.return_array()
			else:
				print(f'Entered length {pos2} is greater than the maximum length of Array rows')
		else:
			print(f'Entered length {pos1} can not be more than no of elements in array')
			
	def search_element(self,element):
		for i in range(self.rows):
			for j in range(self.columns):
				if self.arr_list[i][j]==element:
					print(f'Element {element} is at Row_Number: {i}, Column_Number: {j} ')
					return
		else:
			print(f'Element {element} is not found in Array' )
	def delete_element(self,element,row_pos=None,col_pos=None):
		v_counter=0
		for i in range(len(self.arr_list)):
			if self.arr_list[i].count(element):
				v_counter+=1
		if v_counter>1:
			print(f'Entered {element} has more than one occurance in Array,please specfiy Row_Number and Column_Number ')
		else:
			for i in range(self.rows):
				for j in range(self.columns):
					if self.arr_list[i][j]==element:
						self.arr_list[i][j]=None
						print(f'Element {element} has been deleted from Row_Number: {i}, Column_Number: {j} ')
						return self.return_array()
			else:
				print(f'Element {element} is not found in Array' )



