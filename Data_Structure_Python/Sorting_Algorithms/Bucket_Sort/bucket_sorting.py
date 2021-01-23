import math 
class BucketSort:
	def __init__(self):
		self.bkt_list=[]		

	def add_element(self,value):
		self.bkt_list.append(value)

	def find_max_value(self):
		no_of_bkt=math.ceil(math.sqrt(len(self.bkt_list)))# on then basis of this number, number of list has to be created as doing in line 34,35,36 manually
		for _ in range(len(self.bkt_list)):
			for i in range(len(self.bkt_list)-1):
				a=self.bkt_list[i]
				b=self.bkt_list[i+1]
				if a>b:
					self.bkt_list[i]=b
					self.bkt_list[i+1]=a
		return self.bkt_list[-1],no_of_bkt

	def list_bbl_srt(self,input_list):
		for _ in range(len(input_list)):
			for m in range(len(input_list)-1):
				p=input_list[m]
				q=input_list[m+1]
				if p>q:
					input_list[m]=q
					input_list[m]=p
		return input_list

	def assign_value_to_bucket(self):
		v_max,bkt_cnt=self.find_max_value()
		print(v_max,bkt_cnt)
		a=[]
		b=[]
		c=[]
		for i in range(len(self.bkt_list)):
			if math.ceil((self.bkt_list[i]*bkt_cnt)/v_max)==1:
				a.append(self.bkt_list[i])
			elif math.ceil((self.bkt_list[i]*bkt_cnt)/v_max)==2:
				b.append(self.bkt_list[i])
			elif math.ceil((self.bkt_list[i]*bkt_cnt)/v_max)==3:
				c.append(self.bkt_list[i])
		a=self.list_bbl_srt(a)
		b=self.list_bbl_srt(b)
		c=self.list_bbl_srt(c)
		final_list=a+b+c
		print(final_list)
		
bkt_obj=BucketSort()
bkt_obj.add_element(70)
bkt_obj.add_element(50)
bkt_obj.add_element(60)
bkt_obj.add_element(20)
bkt_obj.add_element(10)
bkt_obj.add_element(200)
bkt_obj.assign_value_to_bucket()