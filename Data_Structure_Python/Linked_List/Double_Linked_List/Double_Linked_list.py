class Node():
	"""Defining a Node for Doubly linked List"""
	def __init__(self,value):
		self.value=value
		self.prev_node=None
		self.next_node=None

class DoubleLinkedList():
	""" A class and object Pointing to Doubly linked List"""
	def __init__(self):
		self.head=None
	#Adding Element in Doubly linked List in the tail of head	
	def add_element(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head
		while crnt_node.next_node is not None:
			crnt_node=crnt_node.next_node
		node.prev_node=crnt_node
		crnt_node.next_node=node
	#Adding a New Head in Doubly linked List
	def add_head_node(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head
		while crnt_node.next_node is not None:
			break
		crnt_node.prev_node=node
		vnode=crnt_node
		node.next_node=vnode
		crnt_node=node
		self.head=crnt_node
	#Adding a New tail in Doubly linked List
	def add_tail_node(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node is None:
				break
			crnt_node=crnt_node.next_node
		node.prev_node=crnt_node
		crnt_node.next_node=node
	#Adding a New node in between in Doubly linked List
	def add_bw_node(self,aftr_node_value,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head
		while True:
			if crnt_node.value==aftr_node_value:
				half_node=crnt_node.next_node
				break
			crnt_node=crnt_node.next_node
		node.prev_node=crnt_node
		half_node.prev_node=node
		node.next_node=half_node
		crnt_node.next_node=node
	#Deleting a Head node in Doubly linked List
	def del_head_node(self):
		if self.head is None:
			print('Empty Double Linked List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node is not None:
				half_node=crnt_node.next_node
				break
			crnt_node=crnt_node.next_node
		#crnt_node.prev_node=None
		crnt_node.next_node=half_node
		half_node.prev_node=None
		self.head=crnt_node.next_node
	#Deleting a tail node in Doubly linked List
	def del_tail_node(self):
		if self.head is None:
			print('Empty Double Linked List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node.next_node is None:
				crnt_node.next_node=None
				break
			crnt_node=crnt_node.next_node
	#Deleting a in between node in Doubly linked List
	def del_inbw_node(self,inbw_node_value):
		if self.head is None:
			print('Empty Double Linked List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node.value==inbw_node_value:
				half_node=crnt_node.next_node.next_node
				break
			crnt_node=crnt_node.next_node
		half_node.prev_node=crnt_node
		crnt_node.next_node=half_node
	#Traversing node to node in Doubly linked List
	def print_dllist(self):
		crnt_node=self.head
		while True:
			print(crnt_node.value,end='->')
			if crnt_node.next_node is None:
				break
			crnt_node=crnt_node.next_node
		print('None')
	#Traversing previous nodes in Doubly linked List
	def print_previous_node(self):
		crnt_node=self.head
		while crnt_node.next_node is not None:
			if crnt_node.prev_node is None:
				print(f'{crnt_node.prev_node}<-',end='')
			else:
				print(f'{crnt_node.prev_node.value}<-',end='')
			crnt_node=crnt_node.next_node
		print(crnt_node.prev_node.value)

dllist=DoubleLinkedList()
dllist.add_element(10)
dllist.print_dllist()
dllist.add_element(20)
dllist.print_dllist()
dllist.add_element(30)
dllist.print_dllist()
dllist.add_element(40)
dllist.print_dllist()
#dllist.print_previous_node()
dllist.add_head_node(5)
dllist.print_dllist()
#dllist.print_previous_node()
dllist.add_tail_node(50)
dllist.print_dllist()
#dllist.print_previous_node()
dllist.add_bw_node(40,45)
dllist.print_dllist()
dllist.del_head_node()
dllist.print_dllist()
#dllist.print_previous_node()
dllist.del_tail_node()
dllist.print_dllist()
#dllist.print_previous_node()
dllist.del_inbw_node(30)
dllist.print_dllist()
dllist.print_previous_node()