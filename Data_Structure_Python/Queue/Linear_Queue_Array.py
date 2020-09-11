class Queue:
	def __init__(self):
		self.v_list=[]

	def enqueue(self,value):
		self.v_list.append(value)

	def dequeue(self):
		if len(self.v_list)==0:
			print('Queue is Empty')
			return
		self.v_list.pop(0)

	def print_queue(self):
		print(self.v_list)

	def size_of_queue(self):
		return print(len(self.v_list))

object_queue=Queue()
object_queue.enqueue(0)
object_queue.enqueue(1)
object_queue.enqueue(2)
object_queue.enqueue(3)
object_queue.enqueue(4)
object_queue.enqueue(5)
object_queue.print_queue()
object_queue.dequeue()
object_queue.print_queue()
object_queue.dequeue()
object_queue.print_queue()
object_queue.size_of_queue()