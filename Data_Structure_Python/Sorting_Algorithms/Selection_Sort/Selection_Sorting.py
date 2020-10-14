class SelectionSort:
	def __init__(self):
		self.ssrt_list=[]

	def add_element(self,value):
		self.ssrt_list.append(value)

	def convert_into_ssrt(self):
		for i in range(len(self.ssrt_list)):
			srt_ary=i
			for j in range(i+1,len(self.ssrt_list)):
				if self.ssrt_list[srt_ary]>self.ssrt_list[j]:
					srt_ary=j
			self.ssrt_list[i],self.ssrt_list[srt_ary]   =self.ssrt_list[srt_ary],self.ssrt_list[i]
	def print_ssrt(self):
		print(self.ssrt_list)

ssrt_obj=SelectionSort()
ssrt_obj.add_element(70)
ssrt_obj.add_element(50)
ssrt_obj.add_element(60)
ssrt_obj.add_element(20)
ssrt_obj.add_element(10)
ssrt_obj.add_element(90)
ssrt_obj.print_ssrt()
ssrt_obj.convert_into_ssrt()
ssrt_obj.print_ssrt()