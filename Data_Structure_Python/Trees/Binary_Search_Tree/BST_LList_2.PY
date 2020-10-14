class Node():
	def __init__(self,value):
		self.value=value
		self.left_child=None
		self.right_child=None

class BTree():
	def __init__(self):
		self.head_node=None
		self.queue_list=[]

	def build_bst(self,value):
		self.push_btree_element(value,self.head_node)

	def push_btree_element(self,value,crnt_node):
		if crnt_node is None:
			crnt_node=Node(value)
			self.head_node=crnt_node
			return
		if crnt_node.value>value:
			if crnt_node.left_child is None:
				crnt_node.left_child=Node(value)			
			self.push_btree_element(value,crnt_node.left_child)
		elif crnt_node.value<value:
			if crnt_node.right_child is None:
				crnt_node.right_child=Node(value)			
			self.push_btree_element(value,crnt_node.right_child)

	def preorder_traversal(self):
		self.pre_order_traversal(self.head_node)
	def postorder_travesal(self):
		self.post_order_traversal(self.head_node)
	def inorder_traversal(self):
		self.in_order_traversal(self.head_node)

	def levelorder_traversal(self):
		#self.queue_list.append(self.head_node.value)
		self.level_order_traversal(self.head_node)
		

	def pre_order_traversal(self,crnt_node):
		if crnt_node:
			print(crnt_node.value,end='->')
			self.pre_order_traversal(crnt_node.left_child)
			self.pre_order_traversal(crnt_node.right_child)
		
	def post_order_traversal(self,crnt_node):
		if crnt_node:
			self.post_order_traversal(crnt_node.left_child)
			self.post_order_traversal(crnt_node.right_child)
			print(crnt_node.value,end='->')

	def in_order_traversal(self,crnt_node):
		if crnt_node:
			self.in_order_traversal(crnt_node.left_child)
			print(crnt_node.value,end='->')
			self.in_order_traversal(crnt_node.right_child)

	def level_order_traversal(self,crnt_node):
		queue_list=[]
		queue_list.append(crnt_node)
		while queue_list:			
			if crnt_node.left_child:
				queue_list.append(crnt_node.left_child)				
				queue_list.append(crnt_node.right_child)			
			queue_list.pop(0)
			print(crnt_node.value ,end='->')
			if queue_list:
				crnt_node=queue_list[0]

	def delete_node_from_tree(self,value):
		self.delete_tree_nodes(value,self.head_node)

	def delete_tree_nodes(self,value,crnt_node):
		if crnt_node.value>value:
			if crnt_node.left_child.value==value  and crnt_node.left_child.left_child is not None:
				crnt_node.left_child=crnt_node.left_child.left_child
			elif crnt_node.left_child.value==value and crnt_node.left_child.right_child is not None:
				crnt_node.left_child=crnt_node.left_child.right_child
			elif crnt_node.left_child.value==value  :
				crnt_node.left_child=None
			elif crnt_node.right_child.value==value:
				crnt_node.right_child=None
			else:
				self.delete_tree_nodes(value,crnt_node.left_child)
		elif crnt_node.value<value:
			if crnt_node.left_child.value==value  and crnt_node.left_child.left_child is not None:
				crnt_node.left_child=crnt_node.left_child.left_child
			elif crnt_node.left_child==value and crnt_node.left_child.right_child is not None:
				crnt_node.left_child=crnt_node.left_child.right_child
			elif crnt_node.left_child.value==value and crnt_node.left_child.left_child is None and crnt_node.left_child.right_child is None :
				crnt_node.left_child=None
			elif crnt_node.right_child.value==value and crnt_node.right_child.right_child is None and crnt_node.right_child.left_child is None:
				crnt_node.right_child=None
			else:
				self.delete_tree_nodes(value,crnt_node.right_child)
		elif crnt_node.value==value and crnt_node.left_child is not None and crnt_node.right_child is not None:

			vnode=self.fn_get_successor(crnt_node.right_child)
			crnt_node.value=vnode.value

	def fn_get_successor(self,crnt_node):
		while True:
			if not crnt_node.left_child.left_child:
				vnode=crnt_node.left_child
				crnt_node.left_child=None
				return vnode
			crnt_node=crnt_node.left_child


btree_obj=BTree()
btree_obj.build_bst(25)
btree_obj.build_bst(50)
btree_obj.build_bst(15)
btree_obj.build_bst(10)
#btree_obj.build_bst(4)
btree_obj.build_bst(12)
btree_obj.build_bst(22)
btree_obj.build_bst(18)
btree_obj.build_bst(24)
btree_obj.build_bst(50)
btree_obj.build_bst(35)
btree_obj.build_bst(31)
btree_obj.build_bst(44)
btree_obj.build_bst(70)
btree_obj.build_bst(66)
btree_obj.build_bst(90)
#btree_obj.preorder_traversal()
#btree_obj.postorder_travesal()
#btree_obj.inorder_traversal()
#btree_obj.levelorder_traversal()
btree_obj.delete_node_from_tree(18)
btree_obj.delete_node_from_tree(10)
btree_obj.delete_node_from_tree(25)
#btree_obj.delete_node_from_tree(70)
btree_obj.preorder_traversal()