class Kettle(object):
	def __init__(self , make , price):
		self.make=make
		self.price=price
		self.on= False
		#self.power=1.5
	def fn_switch_on(self):
		self.on=True

kenwood=Kettle('kenwood',12.23)
print(kenwood.make)
print(kenwood.price)
kenwood.price=90.90
print(kenwood.price)
hamilton=Kettle('hamilton',20)
print(hamilton.price)

hamilton.fn_switch_on()
print(hamilton.on)
Kettle.fn_switch_on(kenwood)
print(kenwood.on)

#Kettle.power=1.5
#print(hamilton.power)
kenwood.power=1.5
print(kenwood.power)

print(Kettle.__dict__)
print(kenwood.__dict__)


