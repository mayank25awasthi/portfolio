class Node():
	def __init__(self,value):
		self.value=value
		self.left_child=None
		self.right_child=None
		self.blc_fact=0

class AvlTree():
	def __init__(self):
		self.head_node=None

	def insert_avl_tree(self,value):
		if self.head_node is None:
			self.head_node=Node(value)
			return
		self.build_avl_tree(self.head_node,value)

	def build_avl_tree(self,crnt_node,value):
		if crnt_node:
			if crnt_node.value>value:
				if not crnt_node.left_child:
					crnt_node.left_child=Node(value)
				else:
					self.build_avl_tree(crnt_node.left_child,value)
			else:
				if not crnt_node.right_child:
					crnt_node.right_child=Node(value)
				else:
					self.build_avl_tree(crnt_node.right_child,value)

	def preorder_traversal(self):
		self.pre_order_traversal_avl(self.head_node)

	def pre_order_traversal_avl(self,crnt_node):
		if crnt_node:	
			print(crnt_node.value,end='->')
			self.pre_order_traversal_avl(crnt_node.left_child)
			self.pre_order_traversal_avl(crnt_node.right_child)

	def balance_factor_calculation(self):
		self.calculate_balance_factor(self.head_node)
		#print('\n')
		#self.calculate_balance_factor_right(self.head_node.right_child)

	def calculate_left_child(self,crnt_node):
		counter_left=0
		while True:
			counter_left+=1
			if not crnt_node.left_child:
				break
			crnt_node=crnt_node.left_child
		return counter_left

	def calculate_right_child(self,crnt_node):
		counter_right=0
		while True:
			counter_right+=1
			if not crnt_node.right_child:
				break
			crnt_node=crnt_node.right_child
		return counter_right

	def calculate_balance_factor(self,crnt_node):
		if crnt_node:
			v_count1=self.calculate_left_child(crnt_node)
			v_count2=self.calculate_right_child(crnt_node)
			crnt_node.blc_fact=v_count1-v_count2
			print(crnt_node.blc_fact,end='->')
			self.calculate_balance_factor(crnt_node.left_child)
			self.calculate_balance_factor(crnt_node.right_child)

	def balacing_avl_tree(self):
		self.balance_nodes(self.head_node)

	def balance_nodes(self,crnt_node):
		if crnt_node:
			if crnt_node.left_child.blc_fact>1 or crnt_node.left_child.blc_fact<=-1:
				crnt_node.left_child.right_child=crnt_node.left_child



avl_obj=AvlTree()
avl_obj.insert_avl_tree(100)
avl_obj.insert_avl_tree(80)
avl_obj.insert_avl_tree(200)
avl_obj.insert_avl_tree(70)
avl_obj.insert_avl_tree(90)
avl_obj.insert_avl_tree(50)
avl_obj.insert_avl_tree(40)
avl_obj.insert_avl_tree(60)
avl_obj.insert_avl_tree(150)
avl_obj.insert_avl_tree(300)
avl_obj.insert_avl_tree(250)
avl_obj.insert_avl_tree(400)
#avl_obj.balance_factor_calculation()
avl_obj.preorder_traversal()
print('\n')
avl_obj.balance_factor_calculation()