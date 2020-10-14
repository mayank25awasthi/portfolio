class Node():
	def __init__(self,value):
		self.value=value
		self.left_node=None
		self.right_node=None

class BTree():
	def __init__(self):
		self.root_node=None
		self.pre_order_list=[]

	#Function to Build a Binary Search Tree
	def push_element(self,value):
		node=Node(value)
		if self.root_node is None:
			self.root_node=node
			return
		else:
			self.recursion_insert(value,self.root_node)
	#Function to Push Data as per the Binary Search Tree Property.
	def recursion_insert(self,value,crnt_node):
		node=Node(value)
		if node.value<crnt_node.value:
			if crnt_node.left_node is None:				
				crnt_node.left_node=node				
			elif crnt_node.left_node is not None and node.value>crnt_node.left_node.value:
				crnt_node.left_node.right_node=node				
			else:
				self.recursion_insert(value,crnt_node.left_node)
		elif node.value>crnt_node.value:
			if crnt_node.right_node is None:
				crnt_node.right_node=node
				
			elif crnt_node.right_node is not None and node.value<crnt_node.right_node.value:
				crnt_node.right_node.left_node=node
			else:
				self.recursion_insert(value,crnt_node.right_node)
		else:
			print('Duplicate Values')
	#Wrapper Function to Build Preorder traveral
	def print_preorder_traversal(self):
		self.preOrder(self.root_node)
		for i in self.pre_order_list:
			print(i,end='->')
		print('None')
	#Wrapper Function to Build Inorder traveral
	def print_inorder_traversal(self):
		self.in_order(self.root_node)
	#Wrapper Function to Build Inorder traveral
	def print_post_order_traversal(self):
		self.post_order(self.root_node)
	#Wrapper Function to Build Level order traveral
	def print_level_order_traversal(self):
		self.level_order(self.root_node)	

	def preOrder(self,crnt_node):
		if crnt_node:
			self.pre_order_list.append(crnt_node.value)
			#print(crnt_node.value,end='->')
			self.preOrder(crnt_node.left_node)
			self.preOrder(crnt_node.right_node)
		
	def in_order(self,crnt_node):
		if crnt_node:			
			self.in_order(crnt_node.left_node)
			print(crnt_node.value,end='->')
			self.in_order(crnt_node.right_node)

	def post_order(self,crnt_node):
		if crnt_node :
			self.post_order(crnt_node.left_node)
			self.post_order(crnt_node.right_node)	
			print(crnt_node.value)
	# Main Function to evaluate a tree in Level Order Traversal.
	def level_order(self,crnt_node):	
		queue_list=[]
		queue_list.append(crnt_node.value)
		while queue_list:
			if crnt_node.left_node:
				queue_list.append(crnt_node.left_node)
			if crnt_node.right_node:
				queue_list.append(crnt_node.right_node)
			queue_list.pop(0)
			print(crnt_node.value,end='->')
			if queue_list:
				crnt_node=queue_list[0]
	#Wrapper Function to delete Leaf Node, One Child Node.
	def delete_node_without_child(self,value):
		self.delete_node(value,self.root_node)
	# Function to delete a leaf node and a Node that has only one child that left child or right child
	def delete_node(self,value,crnt_node):
		if crnt_node.value>value:
			if crnt_node.left_node.value==value and crnt_node.left_node.left_node is None and crnt_node.left_node.right_node is None:
				crnt_node.left_node=None
			elif crnt_node.left_node.value==value and crnt_node.left_node.left_node is not None:				
				crnt_node.left_node=crnt_node.left_node.left_node				
			elif crnt_node.left_node.value==value and crnt_node.left_node.right_node is not None:				
				crnt_node.left_node=crnt_node.left_node.right_node				
			else:
				self.delete_node(value,crnt_node.left_node)
		elif crnt_node.value<value:
			if crnt_node.right_node.value==value and crnt_node.right_node.left_node is None and crnt_node.right_node.right_node is None:				
				crnt_node.right_node=None
			elif crnt_node.right_node.value==value and crnt_node.right_node.left_node is not None:				
				crnt_node.right_node=crnt_node.right_node.left_node
			elif crnt_node.right_node.value==value and crnt_node.right_node.right_node is not None:
				crnt_node.right_node=crnt_node.right_node.right_node
			else:
				self.delete_node(value,crnt_node.right_node)	
		elif crnt_node.value==value and crnt_node.left_node is not None and crnt_node.right_node is not None:			
			successor_node=self.get_successor_node(self.root_node.right_node)			
			self.root_node.value=successor_node.value
			
	# Catch the least node at the right hand side and make it root
	def get_successor_node(self,root_node):
		if root_node.left_node.left_node:
			self.fn_get_least_in_right_node(root_node.left_node)
		else:
			vnode=root_node.left_node
			root_node.left_node=None
			return vnode

tree_obj=BTree()
tree_obj.push_element(70)
tree_obj.push_element(31)
tree_obj.push_element(93)
tree_obj.push_element(34)
tree_obj.push_element(14)
tree_obj.push_element(23)
tree_obj.push_element(73)
tree_obj.push_element(94)
#tree_obj.print_preorder_traversal()
#tree_obj.print_inorder_traversal()
#tree_obj.print_post_order_traversal()
#tree_obj.print_level_order_traversal()
#tree_obj.delete_node_without_child(23)
#tree_obj.delete_node_without_child(23)
#tree_obj.delete_node_without_child(34)
#tree_obj.delete_node_without_child(14)
#tree_obj.delete_node_without_child(70)
tree_obj.print_preorder_traversal()