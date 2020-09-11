class Node():
	def __init__(self,value=None):
		self.value=value
		self.prev_node=None
		self.next_node=None

class CircullarLinkedList():
	def __init__(self):
		self.head=Node(None)
		self.head.next_node=self.head

	def add_tail_node(self,value):
		node=Node(value)
		if self.head.value is None:
			self.head=node
			self.head.next_node=self.head
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node is self.head:
				break
			crnt_node=crnt_node.next_node	
		node.prev_node=crnt_node
		crnt_node.next_node=node
		node.next_node=self.head

	def add_head_node(self,value):
		node=Node(value)
		if self.head.value is None:
			self.head=node
			self.head.next_node=self.head
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node is self.head:
				crnt_node.next_node=node
				break
			crnt_node=crnt_node.next_node
		node.next_node=self.head
		self.head=node
		
	def add_inbw_node(self,aftr_node_value,value):
		node=Node(value)
		if self.head.value is None:
			self.head=node
			self.head.next_node=self.head
			return
		crnt_node=self.head
		while True:
			if  crnt_node.value==aftr_node_value:
				half_node=crnt_node.next_node
				half_node.prev_node=node
				break
			crnt_node=crnt_node.next_node
		node.prev_node=crnt_node
		crnt_node.next_node=node
		node.next_node=half_node

	def del_head_node(self):
		if self.head is None:
			print('Empty Circullar Linked  List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node is self.head:				
				break
			crnt_node=crnt_node.next_node
		crnt_node.next_node=self.head.next_node
		crnt_node.next_node.prev_node=None
		self.head=crnt_node.next_node

	def del_tail_node(self):
		if self.head is None:
			print('Empty Circullar Linked  List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node.next_node is self.head:
				break
			crnt_node=crnt_node.next_node
		crnt_node.next_node=self.head


	def del_inbw_node(self,del_node_value):
		if self.head is None:
			print('Empty Circullar Linked  List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.value==del_node_value:
				half_node=crnt_node.next_node
				break
			crnt_node=crnt_node.next_node
		half_node.prev_node=crnt_node.prev_node
		crnt_node.prev_node.next_node=half_node

	def print_csll(self):
		crnt_node=self.head
		while True:
			print(crnt_node.value,end='->')			
			if crnt_node.next_node==self.head:
				print(crnt_node.next_node.value)
				break		
			crnt_node=crnt_node.next_node	
		print(end='')

	def print_previous_node(self):
		#print(self.head.prev_node,self.head.next_node.prev_node.value,self.head.next_node.next_node.prev_node.value)
		crnt_node=self.head
		while crnt_node.next_node is not self.head:
			if crnt_node.prev_node is None:
				print(crnt_node.prev_node,end='<-')
			else:
				print(crnt_node.prev_node.value,end='<-')
			crnt_node=crnt_node.next_node
		print(crnt_node.prev_node.value)



csll_obj=CircullarLinkedList()
csll_obj.add_tail_node(5)
csll_obj.print_csll()
#csll_obj.print_previous_node()
csll_obj.add_tail_node(10)
csll_obj.print_csll()
csll_obj.add_tail_node(15)
csll_obj.print_csll()
csll_obj.add_tail_node(20)
csll_obj.print_csll()
csll_obj.print_previous_node()
csll_obj.add_head_node(1)
csll_obj.print_csll()
csll_obj.add_tail_node(30)
csll_obj.print_csll()
csll_obj.add_inbw_node(20,25)
csll_obj.print_csll()
csll_obj.del_head_node()
csll_obj.print_csll()
csll_obj.del_head_node()
csll_obj.print_csll()
csll_obj.del_tail_node()
csll_obj.print_csll()
csll_obj.del_inbw_node(20)
csll_obj.print_csll()
csll_obj.print_previous_node()