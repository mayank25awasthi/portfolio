class HeapSort():
	def __init__(self):
		self.hst_list=[None]
		self.final_list=[]

	def add_element(self,value):
		self.hst_list.append(value)

	def build_hst(self):
		for _ in range((len(self.hst_list)//2)):
			self.convert_into_hst()

	def get_left_child(self,idx):
		for m in range(len(self.hst_list)):
			if m==2*idx:
				return self.hst_list[2*idx]
		return 999

	def get_right_child(self,idx):
		for m in range(len(self.hst_list)):
			if m==2*idx+1:
				return self.hst_list[2*idx+1]
		return 999

	def convert_into_hst(self):
		i=1
		while i<=len(self.hst_list)//2:	
			left_child=self.get_left_child(i)
			right_child=self.get_right_child(i)	
			if self.hst_list[i]>=left_child:
				p_val=self.hst_list[i]
				self.hst_list[i]=left_child
				self.hst_list[2*i]=p_val
				#print(self.hst_list)
			elif self.hst_list[i]>=right_child:
				p_val=self.hst_list[i]
				self.hst_list[i]=right_child
				self.hst_list[2*i+1]=p_val
			i=i+1

	def print_hst(self):
		print(self.hst_list)
		print(self.final_list)

	def perform_sorting(self):
		for i in range(1,len(self.hst_list)):
			self.perform_heap_sorting()

	def perform_heap_sorting(self):
		self.final_list.append(self.hst_list[1])
		self.hst_list.pop(1)
		self.build_hst()
		print(self.final_list)

hst_obj=HeapSort()
hst_obj.add_element(10)
hst_obj.add_element(5)
hst_obj.add_element(5)
hst_obj.add_element(30)
hst_obj.add_element(15)
hst_obj.add_element(50)
hst_obj.add_element(25)
hst_obj.add_element(35)
hst_obj.add_element(1)
hst_obj.add_element(100)
hst_obj.build_hst()
hst_obj.perform_sorting()
