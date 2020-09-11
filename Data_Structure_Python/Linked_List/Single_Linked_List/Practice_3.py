class Node():
	def __init__(self,value):
		self.value=value
		self.nextnode=None


class CircullarLinkedList():
	def __init__(self):
		self.head=None

	def add_element(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			self.head.nextnode=self.head
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode ==self.head:
				break
			crnt_node=crnt_node.nextnode		
		crnt_node.nextnode=node
		node.nextnode=self.head

	def add_head_node(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			self.head.nextnode=self.head
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode ==self.head:
				break
			crnt_node=crnt_node.nextnode
		crnt_node.nextnode=node
		node.nextnode=self.head
		self.head=node

	def add_tail_element(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			self.head.nextnode=self.head
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode ==self.head:
				break
			crnt_node=crnt_node.nextnode
		crnt_node.nextnode=node
		node.nextnode=self.head

	def add_inbw_node(self,aftr_node_value,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			self.head.nextnode=self.head
			return
		crnt_node=self.head
		while True:
			if crnt_node.value==aftr_node_value:
				half_node=crnt_node.nextnode
				break
			crnt_node=crnt_node.nextnode
		crnt_node.nextnode=node
		node.nextnode=half_node

	def delete_head_node(self):
		if self.head is None:
			print('Empty Circullar Linked List')
			return
		crnt_node=self.head
		point_node=self.head.nextnode
		while True:
			if crnt_node.nextnode == self.head :
				break
			crnt_node=crnt_node.nextnode
		crnt_node.nextnode=point_node
		self.head=point_node

	def delete_tail_node(self):
		if self.head is None:
			print('Empty Circullar Linked List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode.nextnode==self.head:
				crnt_node.nextnode=crnt_node.nextnode.nextnode
				break
			crnt_node=crnt_node.nextnode

	def delete_inbw_node(self,inbw_node):
		if self.head is None:
			print('Empty Circullar Linked List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode.value==inbw_node:
				crnt_node.nextnode=crnt_node.nextnode.nextnode
				break
			crnt_node=crnt_node.nextnode

	def print_cssl(self):
		crnt_node=self.head
		while True:
			print(crnt_node.value,end='->')
			if crnt_node.nextnode == self.head:
				print(crnt_node.nextnode.value,end='')
				break
			crnt_node=crnt_node.nextnode
		print()

csll=CircullarLinkedList()
csll.add_element(10)
csll.print_cssl()
csll.add_element(20)
csll.print_cssl()
csll.add_element(30)
csll.print_cssl()
csll.add_element(40)
csll.print_cssl()
csll.add_head_node(5)
csll.print_cssl()
csll.add_head_node(3)
csll.print_cssl()
csll.add_tail_element(50)
csll.print_cssl()
csll.add_inbw_node(20,25)
csll.print_cssl()
csll.delete_head_node()
csll.print_cssl()
csll.delete_tail_node()
csll.print_cssl()
csll.delete_tail_node()
csll.print_cssl()
csll.delete_inbw_node(25)
csll.print_cssl()
csll.delete_inbw_node(20)
csll.print_cssl()
