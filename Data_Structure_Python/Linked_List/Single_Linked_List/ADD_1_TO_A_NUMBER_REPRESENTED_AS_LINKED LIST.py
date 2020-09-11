'''Number is represented in linked list such that each digit corresponds to a node in linked list. Add 1 to it. For example 1999 is represented as (1-> 9-> 9 -> 9) 
	and adding 1 to it should change it to (2->0->0->0)

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
Below are the steps :

Reverse given linked list. For example, 1-> 9-> 9 -> 9 is converted to 9-> 9 -> 9 ->1.
Start traversing linked list from leftmost node and add 1 to it. If there is a carry, move to the next node. Keep moving to the next node while there is a carry.
Reverse modified linked list and return head.'''


class Node():
	def __init__(self,value):
		self.value=value
		self.nextnode=None

class LinkedList():
	def __init__(self):
		self.head=None

	def add_element(self,value):
		node=Node(value)
		if self.head is None:
			self.head =node
			return
		crnt_node=self.head
		while crnt_node.nextnode is not None:			
			crnt_node=crnt_node.nextnode
		crnt_node.nextnode=node

	def reverse_llist(self):
		crnt_node=self.head
		if crnt_node == None:
			print('Empty Linkned List')
			return 
		old_node = None
		while crnt_node:
			temp_node = crnt_node.nextnode
			crnt_node.nextnode = old_node
			old_node = crnt_node
			crnt_node = temp_node
		self.head = old_node

	def converted_llist(self):
		crnt_node=self.head
		carry_value=0
		while True:
			#print(crnt_node.value)
			if (crnt_node.value+1)%10==0:
				carry_value=1
				crnt_node.value=0
				print(crnt_node.value,end='->')
			else:
				print(crnt_node.value+carry_value,end='->')
			if crnt_node.nextnode is  None:
				break
			crnt_node=crnt_node.nextnode
		print('None')

	def print_llist(self):
		crnt_node=self.head
		while True:
			print(crnt_node.value,end='->')
			if crnt_node.nextnode is None:
				break
			crnt_node=crnt_node.nextnode
		print('None')


list_convert=LinkedList()
list_convert.add_element(1)
list_convert.print_llist()
list_convert.add_element(9)
list_convert.print_llist()
list_convert.add_element(9)
list_convert.print_llist()
list_convert.add_element(9)
list_convert.print_llist()

list_convert.reverse_llist()
list_convert.print_llist()
list_convert.converted_llist()
