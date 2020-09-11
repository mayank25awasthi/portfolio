class PlayerCharacter(object):
	membership=True
	def __init__(self, name,age):
		if self.membership:
			self.name=name
			self.age=age
	def fn_shout(self):
		print(f'Hi My Name is {self.name}')

	def fn_run(self):
		print(f'Hi My Name is {self.name}')

	@classmethod
	def fn_class_method(self,num1,num2):
		return self('krishna',num1+num2)
	@staticmethod
	def fn_static_method(num1,num2):
		return num1+num2

player3=PlayerCharacter.fn_class_method(3,4)
print(player3.name,player3.age)

player4=PlayerCharacter.fn_class_method(5,6)
print(player4.name,player4.age)