class Node():
	def __init__(self,value):
		self.value=value
		self.next_node=None 

class SingleLinkedList():
	def __init__(self):
		self.head=None

	def push_element(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			return
		crnt_node=self.head		
		while crnt_node.next_node is not None:
			break				
		node.next_node=crnt_node
		crnt_node=node
		self.head=crnt_node

	def pop_stack_element(self):
		crnt_node=self.head
		if self.head is None:
			print('Empty Stack')
			return
		self.head=crnt_node.next_node

	def peek_element(self):
		crnt_node=self.head.value
		print(crnt_node)

	def stack_isempty(self):
		if self.head is None:
			print(True)
		else:
			print(False)

	def print_stack_sll(self):
		crnt_node=self.head
		while True:
			print(crnt_node.value,end='->')
			if crnt_node.next_node is  None:				
				break
			crnt_node=crnt_node.next_node
		print('None')


stack_obj=SingleLinkedList()
stack_obj.push_element(50)
stack_obj.print_stack_sll()
stack_obj.push_element(40)
stack_obj.print_stack_sll()
stack_obj.push_element(30)
stack_obj.print_stack_sll()
stack_obj.push_element(20)
stack_obj.print_stack_sll()
stack_obj.pop_stack_element()
stack_obj.print_stack_sll()
stack_obj.pop_stack_element()
stack_obj.print_stack_sll()
stack_obj.peek_element()
stack_obj.stack_isempty()