class MergeSort:
	def __init__(self):
		self.ms_list=[]
		self.temp_list=[]
	def add_element(self,value):
		self.ms_list.append(value)

	def perform_merge_sort(self):
		self.break_list(self.ms_list)

	def break_list(self,v_list):	
		if len(v_list)>1:
			divider=round(len(v_list)/2)
			self.break_list(v_list[:divider:])
			self.break_list(v_list[divider::])
		else:	
			for m in range(len(self.ms_list)):
				if self.ms_list[m]>v_list[0]:
					self.ms_list.insert(m,v_list[0])

		print(self.ms_list)
	def print_mst(self):
		print(self.ms_list)

mst_obj=MergeSort()
mst_obj.add_element(30)
mst_obj.add_element(20)
mst_obj.add_element(40)
mst_obj.add_element(10)
mst_obj.add_element(80)
mst_obj.add_element(50)
mst_obj.add_element(15)
mst_obj.perform_merge_sort()
#mst_obj.print_mst()