class BinaryTree():
	def __init__(self):
		self.b_list=[]
		self.b_list.insert(0,None)
	def create_binary_tree(self,value):
		self.b_list.append(value)
	def print_btree(self):
		for i in self.b_list:
			print(i,end='->')

	def pre_order_travesal(self,k):		
		if len(self.b_list)>=k:
			print(self.b_list[k],end='->')
			k=2*k
			self.pre_order_travesal(k)
		k=1 
btree_obj=BinaryTree()
btree_obj.create_binary_tree(20)
btree_obj.create_binary_tree(100)
btree_obj.create_binary_tree(3)
btree_obj.create_binary_tree(50)
btree_obj.create_binary_tree(15)
btree_obj.create_binary_tree(250)
btree_obj.create_binary_tree(35)
btree_obj.create_binary_tree(222)
#btree_obj.print_btree()
btree_obj.pre_order_travesal(1)

#None->20->100->3->50->15->250->35->222->[Finished in 0.2s]