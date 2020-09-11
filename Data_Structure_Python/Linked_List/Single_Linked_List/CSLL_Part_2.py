class Node:
	def __init__(self,value):
		self.value=value
		self.nextnode=None

class CircullarLinkedList:
	def __init__(self):
		self.head=Node(None)
		self.head.nextnode=self.head

	def add_head_node(self,value):
		node=Node(value)		
		if self.head.value is None:
			self.head=node
			self.head.nextnode=self.head
			return
		crnt_node=node
		last_node=self.head
		while last_node.nextnode is not self.head:
			last_node=last_node.nextnode
		last_node.nextnode=crnt_node
		crnt_node.nextnode=self.head
		self.head=crnt_node

	def add_tail_node(self,value):
		node=Node(value)
		if self.head.value is None:
			self.head=node
			self.head.nextnode=self.head
			return
		crnt_node=node
		last_node=self.head
		while  last_node.nextnode is not self.head:
			last_node=last_node.nextnode
		vnode=last_node.nextnode
		last_node.nextnode=crnt_node
		crnt_node.nextnode=vnode
		self.head=vnode

	def add_after_node(self,aftr_node,value):
		node=Node(value)
		if self.head.value is None:
			self.head=node
			self.head.nextnode=self.head
			return
		crnt_node=node
		last_node=self.head
		while True:
			if last_node.value==aftr_node:
				crnt_node.nextnode=last_node.nextnode
				last_node.nextnode=crnt_node
				break
			last_node=last_node.nextnode

	def add_before_node (self,bfr_node,value):
		node=Node(value)
		if self.head.value is None:
			self.head=node
			self.head.nextnode=self.head
			return
		crnt_node=node
		last_node=self.head
		while True:
			if last_node.nextnode.value==bfr_node:
				crnt_node.nextnode=last_node.nextnode
				last_node.nextnode=crnt_node
				break
			last_node=last_node.nextnode
	def del_head_node(self):
		if self.head.value is None:
			self.head=node
			self.head.nextnode=self.head
			return
		last_node=self.head
		while last_node.nextnode is not self.head:
			last_node=last_node.nextnode
		last_node.nextnode=self.head.nextnode
		self.head=last_node.nextnode

	def del_tail_node(self):
		if self.head.value is None:
			self.head=node
			self.head.nextnode=self.head
			return
		last_node=self.head.nextnode
		while last_node.nextnode.nextnode is not self.head:
			last_node=last_node.nextnode
		last_node.nextnode=self.head

	def del_bw_node(self,bw_node):
		if self.head.value is None:
			self.head=node
			self.head.nextnode=self.head
			return
		last_node=self.head
		while True:
			if last_node.nextnode.value==bw_node:
				last_node.nextnode=last_node.nextnode.nextnode
				break
			last_node=last_node.nextnode
				
	def print_linked_list(self):
		crnt_node=self.head
		while True:
			print(crnt_node.value,end='->')
			crnt_node=crnt_node.nextnode
			if crnt_node==self.head:
				print(crnt_node.value)
				break			
		print(end='')
			
csll=CircullarLinkedList()
csll.add_head_node(10)
csll.print_linked_list()
csll.add_head_node(20)
csll.print_linked_list()
csll.add_head_node(30)
csll.print_linked_list()
csll.add_head_node(40)
csll.print_linked_list()
csll.add_head_node(50)
csll.print_linked_list()
csll.add_tail_node(5)
csll.print_linked_list()
csll.add_tail_node(3)
csll.print_linked_list()
csll.add_after_node(20,15)
csll.print_linked_list()
csll.add_before_node(20,25)
csll.print_linked_list()
csll.del_head_node()
csll.print_linked_list()
csll.del_head_node()
csll.print_linked_list()
csll.del_tail_node()
csll.print_linked_list()
csll.del_tail_node()
csll.print_linked_list()
csll.del_bw_node(15)
csll.print_linked_list()
csll.del_bw_node(25)
csll.print_linked_list()