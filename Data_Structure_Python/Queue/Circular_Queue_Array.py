class CircularQueue():
	def __init__(self):
		"""Class to hold the Postions for insert and delete"""
		self.start_pointer=0
		self.end_pointer=-1
		self.queue_list=[]
	"""Storing the element in Circular order, with circular we can remove empty Block"""
	def enqueue(self,value):
		if len(self.queue_list)>10:
			print("Circular Queue is Full")
			return
		"""Checking for Empty Block in Array and storing data and reseting the stat end point to process the element"""
		if 'None' in self.queue_list:
			self.queue_list[self.end_pointer]=value
			self.end_pointer+=1
		else:
			self.queue_list.append(value)
			self.end_pointer+=1
	"""Removing element In FIFO order and reseting start ending point"""
	def dequeue(self):
		#self.queue_list.replace(self.queue_list[self.start_pointer],None)
		self.queue_list = [str(sub).replace(str(self.queue_list[self.start_pointer]),'None') for sub in self.queue_list] 
		self.start_pointer+=1
		for i ,j in enumerate(self.queue_list):
			if j=='None':
				self.end_pointer=i
				break
	"""For Printing Queue"""			
	def print_cq(self):
		if len(self.queue_list)>10:
			print("Circular Queue is Full")
			return
		print(self.queue_list,self.start_pointer,self.end_pointer)


cir_object=CircularQueue()
cir_object.enqueue(0)
cir_object.enqueue(1)
cir_object.enqueue(2)
cir_object.enqueue(3)
cir_object.enqueue(4)
cir_object.enqueue(5)
cir_object.enqueue(6)
cir_object.enqueue(7)
cir_object.enqueue(8)
cir_object.enqueue(9)
#cir_object.print_cq()
cir_object.dequeue()
cir_object.dequeue()
cir_object.print_cq()
cir_object.enqueue(15)
cir_object.enqueue(20)
cir_object.print_cq()