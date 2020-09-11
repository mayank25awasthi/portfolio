# rearrange a linked list in such way that all odd position nodes are together and all even positions node are together,
# 1->2->3->4->5->6 , convert it on 1->3->5->2->4->6
class Node():
	def __init__(self,value):
		self.value=value
		self.nextnode=None
#Class Linked List for Pointing Head and Tail
class LinkedList():
	def __init__(self):
		self.head=None
	
	def add_element(self,value):
		node=Node(value)
		if value%2==0:

			if self.head is None:
				self.head=node
				return
			even_node=self.head
			while True:
				if even_node.nextnode is None:
					break
				even_node=even_node.nextnode
			even_node.nextnode=node
		else:
			if self.head is None:
				self.head=node
				return
			odd_node=self.head
			while True:
				if odd_node.nextnode.value%2==0:
					#odd_node=odd_node.nextnode
					break
				odd_node=odd_node.nextnode
			node.nextnode=odd_node.nextnode
			odd_node.nextnode=node
			#print(odd_node.value)


	def print_llist(self):
		crnt_node=self.head		
		while True:
			print(crnt_node.value,end='->')
			if crnt_node.nextnode is None:				
				break
			crnt_node=crnt_node.nextnode
		print('None')
	
sll=LinkedList()
sll.add_element(1)
sll.print_llist()
sll.add_element(2)
sll.print_llist()
sll.add_element(3)
sll.print_llist()
sll.add_element(4)
sll.print_llist()
sll.add_element(5)
sll.print_llist()
sll.add_element(6)
sll.print_llist()
sll.add_element(7)
sll.print_llist()
sll.add_element(8)
sll.print_llist()