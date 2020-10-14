class BubbleSort:
	def __init__(self):
		self.bub_list=[]

	def add_element(self,value):
		self.bub_list.append(value)

	def sort_bub_list(self):
		for _ in self.bub_list:
			for i in range(len(self.bub_list)-1):
				a=self.bub_list[i]
				b=self.bub_list[i+1]
				if a<b:
					pass
				elif a>b:
					self.bub_list[i]=b
					self.bub_list[i+1]=a
					
	def print_list(self):
		print(self.bub_list)

bub_obj=BubbleSort()
bub_obj.add_element(70)
bub_obj.add_element(50)
bub_obj.add_element(60)
bub_obj.add_element(20)
bub_obj.add_element(10)
bub_obj.add_element(90)
bub_obj.sort_bub_list()
bub_obj.print_list()