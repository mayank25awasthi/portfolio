class QuickSort():
	"""docstring for ClassName"""
	def __init__(self):
		self.qst_list=[]

	def add_element(self,value):
		self.qst_list.append(value)

	def print_qst(self):
		print(self.qst_list)

	def perform_quick_sorting(self,v_list):
		pvt=self.qst_partition(v_list)
		vpt=pvt
		if len(v_list)>1:
			self.perform_quick_sorting(v_list[:pvt:])
			#print(v_list,pvt)
			self.perform_quick_sorting(v_list[pvt+1::])
			print(v_list,pvt)
	def qst_partition(self,v_list):
		i=-1
		if len(v_list)>1:
			
			pvt=v_list[-1]
			for p in range(len(v_list)):
				if self.qst_list[p]<=pvt:
					i+=1
					m=self.qst_list[i]
					self.qst_list[i]=self.qst_list[p]
					self.qst_list[p]=m
		return i
		




qs_obj=QuickSort()
qs_obj.add_element(9)
qs_obj.add_element(4)
qs_obj.add_element(6)
qs_obj.add_element(3)
qs_obj.add_element(7)
qs_obj.add_element(1)
qs_obj.add_element(11)
qs_obj.add_element(2)
qs_obj.add_element(5)
qs_obj.print_qst()
qs_obj.perform_quick_sorting(qs_obj.qst_list)
#qs_obj.print_qst()