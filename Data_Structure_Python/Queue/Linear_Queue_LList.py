class Node():
	def __init__(self,value):
		self.value=value
		self.next_node=None 

class LinerQueue():
	def __init__(self):
		self.head=None
		self.tail=None

	def enque_element(self,value):
		node=Node(value)
		if self.head is None:
			self.head=node
			self.tail=node
			return
		crnt_node=self.head
		while True:
			if crnt_node.next_node is None:
				break
			crnt_node=crnt_node.next_node
		tail_node=node
		crnt_node.next_node=node
		#print(tail_node.value)

	def deque_element(self):
		if self.head is None:
			print('Queue is Empty')
			return
		crnt_node=self.head
		while crnt_node.next_node is not None:
			crnt_node=crnt_node.next_node
			break
		self.head=crnt_node


	def reverse_queue(self):
		crnt_node=self.head
		vnode=None
		while crnt_node:
			tmp_node=crnt_node.next_node
			crnt_node.next_node=vnode
			vnode=crnt_node
			crnt_node=tmp_node
		#print('hjn')
		self.head=vnode

	def print_llist_queue(self):
		crnt_node=self.head
		while True:
			print(crnt_node.value,end='->')
			if crnt_node.next_node is None:
				break
			crnt_node=crnt_node.next_node
		print('None')

obj_queue=LinerQueue()
obj_queue.enque_element(10)
obj_queue.print_llist_queue()
obj_queue.enque_element(20)
obj_queue.print_llist_queue()
obj_queue.enque_element(30)
obj_queue.print_llist_queue()
obj_queue.enque_element(40)
obj_queue.print_llist_queue()
obj_queue.enque_element(50)
obj_queue.print_llist_queue()
obj_queue.enque_element(60)
obj_queue.print_llist_queue()
obj_queue.deque_element()
obj_queue.print_llist_queue()
obj_queue.deque_element()
obj_queue.print_llist_queue()
obj_queue.reverse_queue()
obj_queue.print_llist_queue()