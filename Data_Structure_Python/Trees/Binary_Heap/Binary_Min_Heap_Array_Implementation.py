class MinHeap():
	""" Min Heap:-Node values will always be lees than the left and right child """
	def __init__(self):
		#Creating a Array to push heap values
		self.heap_list=[None]
		
	def push_element(self,value):
		self.heap_list.append(value)
	#Getting right child from postion 2x
	def get_left_child(self,index):
		for i in range(len(self.heap_list)):
			if i==2*index:
				return self.heap_list[2*index]
		return 999
	#Getting right child from postion 2x+1
	def get_right_child(self,index):
		for i in range(len(self.heap_list)):
			if i==2*index+1:
				return self.heap_list[2*index+1]
		return 999
	# I have considered a logic node if node will on x index then left child woul bw at 2*x and right child will be at 2*x+1 postion in array
	def re_construct_heap(self):
		for i in range(1,(len(self.heap_list)//2)+1):
			left_child=self.get_left_child(i)
			right_child=self.get_right_child(i)
			if self.heap_list[i]>left_child :
				v_parent=self.heap_list[i]
				self.heap_list[i]=left_child
				self.heap_list[2*i]=v_parent
			elif self.heap_list[i]>right_child:
				v_parent=self.heap_list[i]
				self.heap_list[i]=right_child
				self.heap_list[2*i+1]=v_parent
	#Re cunstructing heap till the heap property satisfies
	def build_min_heap(self):
	  for i in range(len(self.heap_list)//2, 0, -1):
	    self.re_construct_heap()
	#Deleing a root node and trying to rebuild Min Heap with heap property
	def delte_node_heap(self,value):
		if self.heap_list[1]==value:
			self.heap_list[1]=self.heap_list[-1]
			self.heap_list.pop(-1)
			self.build_min_heap()
	#Min Value of Heap
	def min_value(self):
		return self.heap_list[1]
	#Max Value of Heap
	def max_value(self):
		return self.heap_list[-1]
	#size of heap
	def size_of_heap(self):
		return len(self.heap_list)
	#Printin Heap Values
	def print_min_heap(self):
		for i in self.heap_list:
			print(i,end='->')

min_heap_obj=MinHeap()
min_heap_obj.push_element(3)
min_heap_obj.push_element(5)
min_heap_obj.push_element(8)
min_heap_obj.push_element(17)
min_heap_obj.push_element(19)
min_heap_obj.push_element(36)
min_heap_obj.push_element(40)
min_heap_obj.push_element(25)
min_heap_obj.push_element(100)
#insert a node less than root node
#min_heap_obj.push_element(1)
#re structuring heap with heap property
min_heap_obj.build_min_heap()
#deleting a root node
min_heap_obj.delte_node_heap(3)
#re structuring heap with heap property
min_heap_obj.build_min_heap()
#printing heap values
min_heap_obj.print_min_heap()
print('\n')
print(min_heap_obj.min_value(),min_heap_obj.max_value(),min_heap_obj.size_of_heap())
