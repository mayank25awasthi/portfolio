class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self, value):
		self.value=value
		self.next_node=None 

node1=LinkedList(1)
node2=LinkedList(2)
node3=LinkedList(5)
node4=LinkedList(7)
node1.next_node=node2
node2.next_node=node3
node3.next_node=node4
crnt_node=node1
while True:
	print(crnt_node.value,end='->')
	if crnt_node.next_node==None:
		print('None',end='')
		break
	crnt_node=crnt_node.next_node
print()
