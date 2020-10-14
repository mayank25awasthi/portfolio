class BinaryHeapTree():
	""" Min Heap:-Node values will always be lees than the left and right child """
	def __init__(self):
		self.max_heap_list=[None]

	def insert_into_max_heap(self,value):
		self.max_heap_list.append(value)
		#self.re_construct_heap()

	def get_left_child(self,idx):
		for i in range(len(self.max_heap_list)):
			if i==2*idx:
				
				return self.max_heap_list[2*idx]
		return 1

	def get_right_child(self,idx):
		for i in range(len(self.max_heap_list)):
			if i==2*idx+1:
				return self.max_heap_list[2*idx+1]
		return 1
	def re_construct_heap(self):
		for i in range(1,(len(self.max_heap_list)//2)+1):
			left_child=self.get_left_child(i)
			right_child=self.get_right_child(i)
			if self.max_heap_list[i]<left_child:
				v_parent=self.max_heap_list[i]
				self.max_heap_list[i]=left_child
				self.max_heap_list[2*i]=v_parent

			elif self.max_heap_list[i]<right_child:
				v_parent=self.max_heap_list[i]
				self.max_heap_list[i]=right_child
				self.max_heap_list[2*i+1]=v_parent

	#Re cunstructing heap till the heap property satisfies
	def build_max_heap(self):
	  for i in range(len(self.max_heap_list)//2):

	  	self.re_construct_heap()

	def print_max_heap(self):
		for k in self.max_heap_list:
			print(k,end='->')

max_heap_obj=BinaryHeapTree()
max_heap_obj.insert_into_max_heap(100)
max_heap_obj.insert_into_max_heap(40)
max_heap_obj.insert_into_max_heap(50)
max_heap_obj.insert_into_max_heap(10)
max_heap_obj.insert_into_max_heap(15)
max_heap_obj.insert_into_max_heap(45)
max_heap_obj.insert_into_max_heap(40)
max_heap_obj.insert_into_max_heap(300)
max_heap_obj.build_max_heap()
max_heap_obj.print_max_heap()