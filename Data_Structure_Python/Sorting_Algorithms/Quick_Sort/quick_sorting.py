class QuickSort:
	def __init__(self):
		self.qs_list=[]

	def add_element(self,value):
		self.qs_list.append(value)

	def perform_quick_sort(self,v_list):
		pvt=self.qs_implementation(v_list)
		print(pvt,v_list[:pvt:])
		self.qs_implementation(v_list[:pvt:])
	
		self.qs_implementation(v_list[pvt::])

	def qs_implementation(self,v_list):
		if len(v_list)>1:
			pvt=v_list[-1]			
			j=0
		i=-1
		while j<len(self.qs_list):
			if self.qs_list[j]<=pvt:
				i=i+1
				m=self.qs_list[i]
				self.qs_list[i]=self.qs_list[j]
				self.qs_list[j]=m
				print(i)
			j=j+1
		return i
#[1, 2, 4, 3, 5, 6, 11, 9, 7]
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
print(qs_obj.qs_list)
qs_obj.perform_quick_sort(qs_obj.qs_list)
print(qs_obj.qs_list)