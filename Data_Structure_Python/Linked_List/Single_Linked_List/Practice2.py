class Node():
	"""docstring for """
	def __init__(self, value):
		self.value=value
		self.nextnode=None

class SingleLinkedList():
	"""docstring for ClassName"""
	def __init__(self):
		self.head=None

	def add_head_element(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head
		node.nextnode=crnt_node
		crnt_node=node
		self.head=crnt_node

	def add_tail_element(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode is None:
				break
			crnt_node=crnt_node.nextnode
		crnt_node.nextnode=node

	def add_after_node(self,aftr_node_value,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head
		while True:
			if crnt_node.value==aftr_node_value:
				break
			crnt_node=crnt_node.nextnode
		node.nextnode=crnt_node.nextnode
		crnt_node.nextnode=node

	def add_before_node(self,bfr_node_value,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode.value==bfr_node_value:
				break
			crnt_node=crnt_node.nextnode
		node.nextnode=crnt_node.nextnode
		crnt_node.nextnode=node

	def delete_head_node(self):
		if self.head is None:
			print('Empty Single Linked List')
			return
		crnt_node=self.head
		while crnt_node.nextnode is not None:
			break
		crnt_node=crnt_node.nextnode
		self.head=crnt_node

	def delete_tail_node(self):
		if self.head is None:
			print('Empty Single Linked List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode.nextnode is None:
				crnt_node.nextnode=None
				break
			crnt_node=crnt_node.nextnode
	def delete_inbw_node(self,del_node_value):
		if self.head is None:
			print('Empty Single Linked List')
			return
		crnt_node=self.head
		while True:
			if crnt_node.nextnode.value==del_node_value:
				crnt_node.nextnode=crnt_node.nextnode.nextnode
				break
			crnt_node=crnt_node.nextnode
			
	def reverse_linked_list(self):
		if self.head is None:
			print('Empty Single Linked List')
			return
		crnt_node=self.head
		tail_node=None
		while crnt_node:
			temp_node=crnt_node.nextnode
			crnt_node.nextnode=tail_node
			tail_node=crnt_node
			crnt_node=temp_node
		self.head=tail_node			

	def print_Single_linked_list(self):
		crnt_node=self.head
		if crnt_node is None:
			print('Empty Single Linked List')
			return
		while True:
			print(crnt_node.value,end='->')
			if crnt_node.nextnode is None:
				break
			crnt_node=crnt_node.nextnode
		print('None')
		
get_sllist=SingleLinkedList()
get_sllist.add_head_element(10)
get_sllist.print_Single_linked_list()
get_sllist.add_head_element(20)
get_sllist.print_Single_linked_list()
get_sllist.add_head_element(30)
get_sllist.print_Single_linked_list()
get_sllist.add_tail_element(5)
get_sllist.print_Single_linked_list()
get_sllist.add_tail_element(4)
get_sllist.print_Single_linked_list()
get_sllist.add_tail_element(3)
get_sllist.print_Single_linked_list()
get_sllist.add_after_node(20,15)
get_sllist.print_Single_linked_list()
get_sllist.add_after_node(30,25)
get_sllist.print_Single_linked_list()
get_sllist.add_before_node(5,7)
get_sllist.print_Single_linked_list()
get_sllist.delete_head_node()
get_sllist.print_Single_linked_list()
get_sllist.delete_head_node()
get_sllist.print_Single_linked_list()
get_sllist.delete_tail_node()
get_sllist.print_Single_linked_list()
get_sllist.delete_inbw_node(7)
get_sllist.print_Single_linked_list()
get_sllist.reverse_linked_list()
get_sllist.print_Single_linked_list()