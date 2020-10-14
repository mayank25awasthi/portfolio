class Node():
	def __init__(self,value):
		self.value=value
		self.left_child=None
		self.right_child=None
class BinaryTree():
	def __init__(self,value):
		self.head_node=Node(value)

	def btree_traversal(self,crnt_node):	
		queue_list=[]
		queue_list.append(crnt_node.value)
		while queue_list:
			if crnt_node.left_child:
				queue_list.append(crnt_node.left_child)
			if crnt_node.right_child:
				queue_list.append(crnt_node.right_child)
			queue_list.pop(0)
			print(crnt_node.value,end='->')
			if queue_list:
				crnt_node=queue_list[0]

tree_obj=BinaryTree(100)
tree_obj.head_node.left_child=Node(50)
tree_obj.head_node.right_child=Node(200)
tree_obj.head_node.left_child.left_child=Node(25)
tree_obj.head_node.left_child.right_child=Node(75)
tree_obj.head_node.right_child.left_child=Node(250)
tree_obj.head_node.right_child.right_child=Node(300)
tree_obj.btree_traversal(tree_obj.head_node)